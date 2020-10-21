from typing import Union, Optional, Tuple, NamedTuple


# Union[float, None] is the same as Optional[float]
def get_batting_ave(hits: int, at_bats: int) -> Optional[float]:
    if at_bats > 0:
        return round(hits / at_bats, 3)
    else:
        return None


def get_slugging_pct(singles, doubles, triples, home_runs, at_bats):
    numerator = (singles + (2 * doubles) + (3 * triples) + (4 * home_runs))
    return round(numerator / at_bats, 3)


class StatsResult(NamedTuple):
    get_batting_ave: Optional[float]
    slugging_pct: float


def get_stats(singles: int, doubles: int, triples: int, home_runs: int, at_bats: int) -> StatsResult:
    hits = singles + doubles + triples + home_runs
    batting_ave = get_batting_ave(hits, at_bats)
    slugging_pct = get_slugging_pct(singles, doubles, triples, home_runs, at_bats)
    return StatsResult(batting_ave, slugging_pct)


player_ave = get_batting_ave(174, 549)
print("player_ave: {}".format(player_ave))

player2_ave = get_batting_ave(0, 0)
print("player2_ave: {}".format(player2_ave))

player_slg = get_slugging_pct(93, 38, 4, 46, 539)
player_stats = get_stats(93, 38, 4, 46, 539)
print("player_stats: {}".format(player_stats))
print(player_stats.get_batting_ave)
