help:
	@echo "Použijte příkaz \`make <target>' kde <target> je jedno z následujících:"
	@echo "    all        pro vytvoření všech PDF souborů"
	@echo "    1          pro vytvoření PDF k předmětu Kapitálové obchodní korporace"
	@echo "    2          pro vytvoření PDF k předmětu Právo duševního vlastnictví"
	@echo "    3          pro vytvoření PDF k předmětu Tvorba odborného textu"
	@echo "    4          pro vytvoření PDF k předmětu Mezinárodní právo soukromé"
	@echo "    5          pro vytvoření PDF k předmětu Relativní majetková práva - vybrané aspekty"
	@echo "    6          pro vytvoření PDF k předmětu Prevence hospodářské kriminality"
	@echo "    7          pro vytvoření PDF k předmětu Soudní a mimosoudní řešení sporů v OPV"
	@echo "    8          pro vytvoření PDF k předmětu Správa obchodní korporace v úpadku"
	@echo "    9          pro vytvoření PDF k předmětu Strategický a projektový management"
	@echo "    10         pro vytvoření PDF k předmětu Daňové právo v obchodních vztazích"
	@echo "    11         pro vytvoření PDF k předmětu Bezpečnostní hrozby (volitelný předmět)"
	@echo "    12         pro vytvoření PDF k předmětu Diferenční předmět - občanské právo (volitelný předmět)"
	@echo "    13         pro vytvoření PDF k předmětu Statistická data ve Veřejném sektoru (volitelný předmět)"
	@echo "    14         pro vytvoření PDF k předmětu e-Government v teorii a praxi"

# Složka pro Kapitálové obchodní korporace
1:
	make -C 1-rocnik-1-trimestr-kapitalove-obchodni-korporace

# Složka pro Právo duševního vlastnictví
2:
	make -C 1-rocnik-1-trimestr-pravo-dusevniho-vlastnictvi

# Složka pro Tvorbu odborného textu
3:
	make -C 1-rocnik-1-trimestr-tvorba-odborneho-textu

# Složka pro Mezinárodní právo soukromé
4:
	make -C 1-rocnik-2-trimestr-mezinarodni-pravo-soukrome

# Složka pro Relativní majetková práva - vybrané aspekty
5:
	make -C 1-rocnik-2-trimestr-relativni-majetkova-prava-vybrane-aspekty

# Složka pro Prevence hospodářské kriminality
6:
	make -C 2-rocnik-1-trimestr-prevence-hospodarske-kriminality

# Složka pro Soudní a mimosoudní řešení sporů v OPV
7:
	make -C 2-rocnik-1-trimestr-soudni-a-mimosoudni-reseni-sporu-v-OPV

# Složka pro Správa obchodní korporace v úpadku
8:
	make -C 2-rocnik-1-trimestr-sprava-obchodni-korporace-v-upadku

# Složka pro Strategický a projektový management
9:
	make -C 2-rocnik-1-trimestr-strategicky-a-projektovy-management

# Složka pro Daňové právo v obchodních vztazích
10:
	make -C 2-rocnik-2-trimestr-danove-pravo-v-obchodnich-vztazich

# Složka pro Daňové právo v obchodních vztazích
11:
	make -C 1-rocnik-1-trimestr-bezpecnostni-hrozby

# Složka pro Daňové právo v obchodních vztazích
12:
	make -C 1-rocnik-1-trimestr-diferencni-predmet-obcanske-pravo

# Složka pro Statistická data ve veřejném sektoru
13:
	make -C 1-rocnik-1-trimestr-statisticka-data-ve-verejnem-sektoru

# Složka pro Statistická data ve veřejném sektoru
14:
	make -C 1-rocnik-2-trimestr-e-government-v-teorii-a-praxi

# Vygenerování veškerých poznámek
# all: 1 2 3 4 5 6 7 8 9 10 11 12 13 14
all: 1 2 3 4 5 6 7 8 9 11 12 13 14
