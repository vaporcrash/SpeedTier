from pathlib import Path

import polars as pl
from mcp.server import MCPServer

STATS = pl.read_csv(Path(__file__).parent / "pokemon_champions_base_stats.csv")

mcp = MCPServer("Demo")


@mcp.tool()
def base_stat_total(name: str) -> int:
    """Look up a Pokémon's base stat total (BST) by name, e.g. "Charizard"."""
    rows = STATS.filter(pl.col("name").str.to_lowercase() == name.strip().lower())
    if rows.is_empty():
        raise ValueError(f"No Pokémon named {name!r} in the dataset")
    return rows.item(0, "bst")

@mcp.tool()
def speed_compare(name1: str, name2: str) -> str:
    """Compare the speed of two Pokémon by name."""
    speed1 = base_stat_total(name1)
    speed2 = base_stat_total(name2)
    if speed1 > speed2:
        return f"{name1} is faster than {name2}"
    elif speed1 < speed2:
        return f"{name2} is faster than {name1}"
    else:
        return f"{name1} and {name2} have the same speed"


@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"
