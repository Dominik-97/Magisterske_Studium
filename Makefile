help:
	@echo "Použijte příkaz \`make <target>' kde <target> je jedno z následujících:"
	@echo "    all        pro vytvoření všech PDF souborů"
	@echo "    1          pro vytvoření PDF k předmětu Občanské právo"
	@echo "    2          pro vytvoření PDF k předmětu ..."
	@echo "    3          pro vytvoření PDF k předmětu ..."
	@echo "    4          pro vytvoření PDF k předmětu ..."

# Testovací složka
1:
	make -C Obcanske_Pravo

# Složka pro budoucí předmět
2:
	make -C Slozka2

# Složka pro další budoucí předmět
3:
	make -C Slozka3

# Složka pro ještě další budoucí předmět
4:
	make -C Slozka4

# Vygenerování veškerých poznámek
all: 1 2 3 4
