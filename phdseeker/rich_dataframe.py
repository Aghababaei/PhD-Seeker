# a modified version of https://github.com/khuyentran1401/rich-dataframe/blob/master/rich_dataframe/rich_dataframe.py

import time
from contextlib import contextmanager

import pandas as pd
from rich import print
from rich.box import MINIMAL, SIMPLE, SIMPLE_HEAD, SQUARE
from rich.columns import Columns
from rich.console import Console
from rich.live import Live
from rich.measure import Measurement
from rich.table import Table

console = Console()

BEAT_TIME = 0.008

COLORS = ["cyan", "magenta", "red", "green", "blue", "purple"]


@contextmanager
def beat(length: int = 1) -> None:
    with console:
        yield
    time.sleep(length * BEAT_TIME)


class DataFramePrettify:

    def __init__(
        self,
        df: pd.DataFrame,
        delay_time: int = 5,
        clear_console: bool = True,
    ) -> None:
        self.df = df.reset_index().rename(columns={"index": ""})
        self.df["Country"] = (self.df.index+1).astype(str) + ' ' + self.df["Country"].astype(str)
        self.table = Table(show_footer=False)
        self.table_centered = Columns(
            (self.table,), align="center", expand=True
        )
        self.num_colors = len(COLORS)
        self.delay_time = delay_time
        self.clear_console = clear_console

        self.columns = self.df.columns
        self.rows = self.df.values

        if self.clear_console:
            console.clear()

    def _add_columns(self):
        for col in self.columns[1:]:
            with beat(self.delay_time):
                self.table.add_column(str(col))

    def _add_rows(self):
        for row in self.rows:
            with beat(self.delay_time):
                row = [str(item) for item in row[1:]]
                self.table.add_row(*list(row))

    def _add_random_color(self):
        for i in range(len(self.table.columns)):
            with beat(self.delay_time):
                self.table.columns[i].header_style = COLORS[
                    i % self.num_colors
                ]

    def _add_style(self):
        for i in range(len(self.table.columns)):
            with beat(self.delay_time):
                self.table.columns[i].style = (
                    "bold " + COLORS[i % self.num_colors]
                )

    def _adjust_box(self):
        for box in [SIMPLE_HEAD, SIMPLE, MINIMAL, SQUARE]:
            with beat(self.delay_time):
                self.table.box = box

    def _dim_row(self):
        with beat(self.delay_time):
            self.table.row_styles = ["none", "dim"]

    def _adjust_border_color(self):
        with beat(self.delay_time):
            self.table.border_style = "bright_yellow"

    def _change_width(self):
        original_width = Measurement.get(console, self.table).maximum
        width_ranges = [
            [original_width, console.width, 2],
            [console.width, original_width, -2],
            [original_width, 90, -2],
            [90, original_width + 1, 2],
        ]

        for width_range in width_ranges:
            for width in range(*width_range):
                with beat(self.delay_time):
                    self.table.width = width

            with beat(self.delay_time):
                self.table.width = None

    def _add_caption(self):
        with beat(self.delay_time):
            self.table.caption = f"All [bold green]{len(self.rows)}[/bold green] found positions are shown here."

    def prettify(self):
        with Live(
            self.table_centered,
            console=console,
            refresh_per_second=self.delay_time,
            vertical_overflow="ellipsis",
        ):
            self._add_columns()
            self._add_rows()
            self._add_random_color()
            self._add_style()
            self._adjust_border_color()
            # self._add_caption()

        return self.table


def prettify(
    df: pd.DataFrame,
    delay_time: int = 5,
    clear_console: bool = True,
):
    """Create animated and pretty Pandas DataFrame
    Parameters
    ----------
    df : pd.DataFrame
        The data you want to prettify
    delay_time : int, optional
        How fast is the animation, by default 5. Increase this to have slower animation.
    clear_console: bool, optional
        Clear the console before priting the table, by default True. If this is set to false the previous console input/output is maintained
    """
    if isinstance(df, pd.DataFrame):
        DataFramePrettify(
            df, delay_time,clear_console
        ).prettify()

    else:
        # In case users accidentally pass a non-datafame input, use rich's print instead
        print(df)