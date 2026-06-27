# Feature

## Unify

### Rice

- F: Farmer's Delight
- K: Kaleidoscope_cookery
- T: Tsuki
- C: Create

Now Rice Process is:

K:Wild Rice --> K:Crop ---> K:Rice Panicle + K:Wild Rice --F:Cut or T:Cut--> K:Wild Rice + T:Straw --K:Millstone or T:Mortar or C:Millstone--> T:Brown Rice --Millstone--> K:Rice

K:Wild Rice could be gained from F:Wild Rice or Grass.

- Change Wild Rice Name
  - assets/kaleidoscope_cookery/lang/
- Change Loot Table
  - data/farmersdelight/loot_table/blocks/wild_rice.json
- Cutting Recipe 
  - data/farmersdelight/recipe/cutting/rice_panicle.json
  - data/farmersdelight/recipe/cutting/wild_rice.json
- Millstone
  - data/kaleidoscope_cookery/recipe/integration/create/milling/
  - data/kaleidoscope_cookery/recipe/millstone/
  - data/tsuki/recipe/stone_mortar/

### Misc

youkaisfeasts  > kaleidoscope > farmersdelight > tsuki

- tomato -> kaleidoscope_cookery:tomato
- lemon -> tsuki:lemon
- soybean -> youkaisfeasts:soybean
- matcha, mocha -> youkaisfeasts:matcha
- tomato_seed -> kaleidoscope_cookery:tomato_seeds
- cabbage -> farmersdelight:cabbage
- sliced_cabbage -> farmersdelight:cabbage_leaf
- rice -> kaleidoscope_cookery:rice
- cooked_rice -> kaleidoscope_cookery:cooked_rice
- rice_panicle --> kaleidoscope_cookery:rice_panicle
- rice_seeds --> kaleidoscope_cookery:wild_rice
- whole_wheat_flour, flour -> tsuki:flour
- wheat_dough ->kaleidoscope_cookery:raw_dough
- grape -> kaleidoscope_tavern:grape
- grape_green -> kaleidoscope_tavern:green_grape
- green_tea_leaves -> youkaisfeasts:green_tea_leaves
- pasta -> kaleidoscope_cookery:raw_noodles
- pineapple -> youkaisfeasts:redbean
- tofu -> youkaisfeasts:tofu

## Tags

- tsuki:food_oil_bucket -> #kaleidoscope_cookery:bucket_oil
- minecraft:carrot -> #c:foods/carrot

## Recipe Convert

### Cooking

- youkaisfeasts:unordered_cooking -> tsuki:cooking

### Brew

- tsuki:fermenting, youkaisfeasts:simple_fermentation -> brewinandchewin:fermenting
- brewinandchewin:fermenting, youkaisfeasts:simple_fermentation -> tsuki:fermenting
- brewinandchewin:fermenting, tsuki:fermenting -> youkaisfeasts:simple_fermentation

## Recipe Change

## Recipe Fix

- Fix mynethersdelight:crafting/raw_stuffed_hoglin_from_kaleidoscope from Kaleidoscope Nether
- Fix series built-in datapack bugs

## Language Change
