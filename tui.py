from textual.app import App
from typing import TYPE_CHECKING

from textual.widgets import Placeholder, Static, Header,Footer, ScrollView
from textual import events
from textual_inputs import IntegerInput, TextInput
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.console import Console, ConsoleOptions, RenderableType
from rich.padding import PaddingDimensions
from textual.reactive import Reactive
from googleApis import *
import re
import warnings
warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
from textual.message import Message

class CustomHeader(Header):
    """Override the default Header for Styling"""

    def __init__(self) -> None:
        super().__init__()
        self.tall = False

    def render(self) -> RenderableType:
        header_table = Table.grid(padding=(0, 1), expand=True)
        header_table.style = self.style
        header_table.add_column(justify="left", ratio=0, width=8)
        header_table.add_column("title", justify="center", ratio=1)
        header_table.add_column("clock", justify="right", width=8)
        header_table.add_row(
            "☕", self.full_title, self.get_clock() if self.clock else ""
        )
        header: RenderableType
        header = Panel(header_table, style=self.style) if self.tall else header_table
        return header
    async def on_click(self, event: events.Click) -> None:
        return await super().on_click(event)

class CustomFooter(Footer):
    """Override the default Footer for Styling"""

    def make_key_text(self) -> Text:
        """Create text containing all the keys."""
        text = Text(
            style="white on rgb(98,98,98)",
            no_wrap=True,
            overflow="ellipsis",
            justify="left",
            end="",
        )
        for binding in self.app.bindings.shown_keys:
            key_display = (
                binding.key.upper()
                if binding.key_display is None
                else binding.key_display
            )
            hovered = self.highlight_key == binding.key
            key_text = Text.assemble(
                (f" {key_display} ", "reverse" if hovered else "default on default"),
                f" {binding.description} ",
                meta={"@click": f"app.press('{binding.key}')", "key": binding.key},
            )
            text.append_text(key_text)

        # end_text = Text(
        #     text="Akash-Sharma",
        #     style="white on rgb(98,98,98)",
        #     no_wrap=True,
        #     overflow="ellipsis",
        #     justify="right",
        #     end="",
        # )
        # text.append_text(end_text)
        return text

class GcalInp(TextInput):
    def __init__(self, output):
        super(GcalInp, self).__init__(placeholder=">>>", name="gcalOption")
        self.gcalOut = output

    async def on_key(self, event: events.Key) -> None:
        if event.key == "enter":
            new_input = self.value
            await self.gcalOut.update(self.handler(new_input))
            self.value = ""

    def handler(self, value):
        if(value == "agenda"):
            ni = cal_events()
            new_Panel = Panel(ni, title="📆 Google Calendar")
            return new_Panel
        elif (value == "table"):
            from rich.table import Table
            table = Table(show_header=True, header_style="bold magenta")
            table.title = "[not italic] 📆 Google Calendar [/]"
            table.add_column("Language", justify="right", style="bright_yellow", no_wrap=True)
            table.add_column("Year Initially Released", style="green")
            table.add_column("Most recent version", justify="right", style="red")
            table.add_row("", "Python", "1991", "3.9.1")
            table.add_row("", "R", "1993", "4.0.3")
            table.add_row("", "Java", "1995", "Java 15")
            
            return table
        else: 
            new_Panel = Panel(value, title="📆 Google Calendar")
            return new_Panel


class GtaskInp(TextInput):
    def __init__(self, output):
        super(GtaskInp, self).__init__(placeholder=">>>", name="gtaskOption")
        self.gtaskOut = output

    async def on_key(self, event: events.Key) -> None:
        if event.key == "enter":
            new_input = self.value
            await self.gtaskOut.update(self.handler(new_input))
            self.value = ""

    def handler(self, value):
        ni = value
        if "tasklists" in value:
            ni = tasks_lists("tasklists",0)
            
        elif "tasks" in value: 
            taskid = 0
            if "--" in value :
                match = re.search('--(\d+)', value)
                if match:
                    taskid = int(match.group(1))
                else : 
                    taskid = 0
            else :
                taskid = 0

            ni = tasks_lists("tasks",taskid)

        new_Panel = Panel(ni, title="✅ Google Tasks")
        return new_Panel

class GkeepInp(TextInput):
    def __init__(self, output):
        super(GkeepInp, self).__init__(placeholder=">>>", name="gkeepOption")
        self.gkeepOut = output

    async def on_key(self, event: events.Key) -> None:
        if event.key == "enter":
            new_input = self.value
            new_Panel = Panel(new_input, title="📒 Google Keep Journalling")
            await self.gkeepOut.update(new_Panel)
            self.value = ""
		
class HabiticaInp(TextInput):
    def __init__(self, output):
        super(HabiticaInp, self).__init__(placeholder=">>>", name="habitOption")
        self.habiticaOut = output

    async def on_key(self, event: events.Key) -> None:
        if event.key == "enter":
            new_input = self.value
            new_Panel = Panel(new_input, title="🎯 Habit Tracking")
            await self.habiticaOut.update(new_Panel)
            self.value = ""

class PomodoroInp(TextInput):
    def __init__(self, output):
        super(PomodoroInp, self).__init__(placeholder=">>>", name="pomoOption")
        self.pomoOut = output

    async def on_key(self, event: events.Key) -> None:
        if event.key == "enter":
            new_input = self.value
            new_Panel = Panel(new_input, title="⌚ Pomodoro")
            await self.pomoOut.update(new_Panel)
            self.value = ""

class WorkStation(App):
    current_index: Reactive[int] = Reactive(-1)

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.tab_index = ["gcalOption", "gtaskOption", "habitOption", "gkeepOption", "pomoOption"]

    async def on_load(self):
        await self.bind("q", "quit", "Quit")
        await self.bind("ctrl+i", "next_tab_index", show=False)
        await self.bind("tab", "", "Navigate")
        await self.bind("shift+tab", "previous_tab_index", "Navigate Back", show = False)
        await self.bind("escape", "reset_focus", "Reset Focus", show=False)
        await self.bind("shift+r", "quit", "Resync All")
        await self.bind("shift+s", "quit", "Settings")
        await self.bind("shift+h", "quit", "Help")

    async def on_mount(self) -> None:
        self.header = CustomHeader() ## used self for focussing the menu pointer
        await self.view.dock(self.header, edge="top")
        await self.view.dock(CustomFooter(), edge="bottom")


        grid = await self.view.dock_grid()
        grid.add_column(name="left")
        grid.add_column(name="center")
        grid.add_column(name="right")
        # rows
        grid.add_row(fraction=15,name="top")
        grid.add_row(fraction=3,name="optionsFor3")
        grid.add_row(fraction=3,name="bottomHalf")
        grid.add_row(fraction=3,name="optionsFor12")
        grid.add_row(fraction=10,name="bottom")
        grid.add_row(fraction=3,name="optionsFor45")



        grid.add_areas(
            area1="left,top-start|optionsFor12-end",
            area2="center,top-start|optionsFor12-end",
            area3="right,top-start|optionsFor3-end",
            area4="left-start|center-end,bottom-start|optionsFor45-end",
            area5="right,bottomHalf-start|optionsFor45-end",
            optionsFor1="left,optionsFor12",
            optionsFor2="center,optionsFor12",
            optionsFor3="right,optionsFor3",
            optionsFor4="right,optionsFor45",
            optionsFor5="left-start|center-end,optionsFor45"
        )



        self.gcal =  Static(
            renderable=Panel(
                "", title="📆 Google Calendar")
        )

        # await self.view.dock(self.gcal, edge="left", size=40)
        self.gtask = Static(
            renderable=Panel(
                "", title="✅ Google Tasks")
        )
        self.gkeep = Static(
            renderable=Panel(
                "", title="📒 Google Keep Journalling")
        )
        # await self.view.dock(self.gtask, self.gkeep, edge="top")
        self.habitica = Static(
            renderable=Panel(
                "", title="🎯 Habit Tracking")
        )

        self.pomodoro = Static(
            renderable=Panel(
                "", title="⌚ Pomodoro")
        )

        self.gcalOption = GcalInp(self.gcal)
        self.gtaskOption = GtaskInp(self.gtask)
        self.habitOption = HabiticaInp(self.habitica)
        self.pomoOption = PomodoroInp(self.pomodoro)
        self.gkeepOption = GkeepInp(self.gkeep)



        grid.place(
            area1=self.gcal,
            area2=self.gtask,
            area3=self.habitica,
            area4=self.gkeep,
            area5=self.pomodoro,
            optionsFor1=self.gcalOption,
            optionsFor2=self.gtaskOption,
            optionsFor3=self.habitOption,
            optionsFor4=self.pomoOption,
            optionsFor5=self.gkeepOption
        )


    async def action_next_tab_index(self) -> None:
        """Changes the focus to the next form field"""
        if self.current_index < len(self.tab_index) - 1:
            self.current_index += 1
            await getattr(self, self.tab_index[self.current_index]).focus()

    async def action_previous_tab_index(self) -> None:
        """Changes the focus to the previous form field"""
        if self.current_index > 0:
            self.current_index -= 1
            await getattr(self, self.tab_index[self.current_index]).focus()

    async def action_reset_focus(self) -> None:
        self.current_index = -1
        await self.header.focus()
    
    async def handle_input_on_focus(self, message: Message) -> None:
        self.current_index = self.tab_index.index(message.sender.name)


if __name__ == "__main__":
    WorkStation.run(title="Dash⚡Term", log="DashTerm.log")
