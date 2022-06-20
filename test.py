import pathlib

import random, string


def randomname(n):
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))


def writeRandomText(file):
    f = open(file, "w")
    f.write(str(randomname(5)))
    f.close()


BASE_DIR = pathlib.Path(__file__).parent


print(f"BASE_DIR:{BASE_DIR}")

print(type(BASE_DIR))


def Generate_dummy_files():
    new_files = [] = jls_extract_def()
    for y in range(1, 5):
        year_dir = BASE_DIR / "DATA" / f"year200{y}"
        year_dir.mkdir()
        for m in range(1, 13):
            month_dir = year_dir / f"month{m}"
            month_dir.mkdir()
            for d in range(1, 31):
                day_dir = month_dir / f"day{d}"
                day_dir.mkdir()
                new_file = day_dir / f"{y}-{m}-{d}_NewFile.csv"
                new_file.touch()
                writeRandomText(new_file)


# Scan files
p = pathlib.Path(BASE_DIR)
print(list(p.glob("**/*.csv").name))
