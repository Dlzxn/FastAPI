from models.db import insert_post, read_posts, read_project, insert_project


insert_post("FUUUCK", "fffusuf", "https:[eafafa")
insert_post("FUUfagagwagaK", "ffw344uf", "htttf6eafafa")
insert_post("FwafafwawfUCK", "faawt3rwfusuf", "ht4w33fa")
a = read_posts()
print(len(a))
print(f"posts: {a}")

insert_project(1, "rwr", "warafaw", "awrararawr", "aawfafaw")
insert_project(2, "rwr", "warafaw", "awrararawr", "aawfafaw")
a = read_project()
print(a)