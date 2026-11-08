# GOG DB Data Dictionary

Source: https://www.gogdb.org/

Each product folder can contain `product.json`, `prices.json`, `prices_pre2019.json`, `changes.json` and a `builds/` folder.

file | count
-------|---------
product folders | 15,648
product.json | 15,579
changes.json | 15,647
prices.json | 13,610
prices_pre2019.json | 5,830 (3,060 of them empty)
builds/*.json | 71,948

The tables and how they relate are drawn in the [entity relationship diagram](erd.md).

>Nested fields are written as `parent.child`. 
## product.json

One object per product.

column | description
-------|---------
id | GOG product ID. Matches the folder name.
title | Product name as shown on the store.
slug | URL-friendly name used in store links.
type | Kind of product: game, dlc or pack.
access | Access level code (0, 1 or 2). Meaning not documented by GOG DB.
added_on | Timestamp when GOG DB first saw the product (UTC, ISO 8601).
last_updated | Timestamp of GOG DB's most recent refresh of the product (UTC, ISO 8601).
global_date | Original worldwide release date of the game.
store_date | Date the product went on sale in the GOG store.
store_state | Store status: default, coming-soon, early-access or preorder.
is_in_development | True if the game is still in development (early access).
is_using_dosbox | True if the game runs through DOSBox.
age_rating | Age rating number.
user_rating | Average user rating score.
rank_bestselling | Position in GOG's bestselling ranking.
rank_trending | Position in GOG's trending ranking.
description | Store description text (may contain HTML).
changelog | Release notes / patch notes text (may contain HTML).
copyright | Copyright and trademark notice.
publisher | Main publisher name.
publishers | List of publisher names.
developers | List of developer names.
series | Game series the product belongs to.
series.id | Series ID.
series.name | Series name.
comp_systems | Operating systems the product supports (windows, osx, linux).
cs_systems | Operating systems with Galaxy content-system builds.
features[] | Store features, e.g. Single-player, Achievements, Cloud saves.
features[].id | Feature ID, e.g. single.
features[].name | Feature display name.
properties[] | Genres listed on the store.
properties[].name | Genre display name.
properties[].slug | Genre URL name.
tags[] | Genre/tag tree.
tags[].id | Tag ID.
tags[].level | Depth in the tag tree (1 = top-level genre, 2 = sub-genre).
tags[].name | Tag display name.
tags[].slug | Tag URL name.
localizations[] | Supported languages.
localizations[].code | Language code, e.g. en.
localizations[].name | Language name.
localizations[].text | True if text/subtitles are translated.
localizations[].audio | True if voice audio is translated.
dlcs | List of product IDs of DLCs for this product.
editions[] | Editions of this product (e.g. Standard, Deluxe).
editions[].id | Product ID of the edition.
editions[].name | Edition name.
editions[].has_product_card | True if the edition has its own store page.
includes_games | List of product IDs included in this pack.
is_included_in | List of product IDs of packs that include this product.
requires | List of product IDs this product needs (e.g. the base game for a DLC).
required_by | List of product IDs that need this product.
builds[] | Summary of every game build. Full build manifests are in `builds/`.
builds[].id | Build ID. Matches a file name in `builds/`.
builds[].product_id | Product the build belongs to.
builds[].generation | Content-system generation (1 = older, 2 = newer).
builds[].legacy_build_id | Older-style build ID.
builds[].os | Operating system of the build.
builds[].branch | Beta/test branch name. Null for the main branch.
builds[].version | Version string set by the developer.
builds[].date_published | Timestamp the build was published.
builds[].listed | True if the build is listed.
builds[].public | True if the build is public.
builds[].tags | List of build tags.
builds[].meta_id | Manifest metadata ID.
builds[].link | URL of the build manifest on GOG's CDN.
dl_installer[] | Downloadable installers.
dl_installer[].id | Installer ID, e.g. installer_windows_en.
dl_installer[].name | Installer name.
dl_installer[].os | Operating system of the installer.
dl_installer[].language.code | Installer language code.
dl_installer[].language.name | Installer language name.
dl_installer[].version | Installer version string.
dl_installer[].total_size | Total size in bytes.
dl_installer[].files[] | Files that make up the installer.
dl_installer[].files[].id | File ID.
dl_installer[].files[].size | File size in bytes.
dl_installer[].files[].downlink | Download API URL of the file.
dl_patch[] | Downloadable patches.
dl_patch[].id | Patch ID.
dl_patch[].name | Patch name.
dl_patch[].os | Operating system of the patch.
dl_patch[].language.code | Patch language code.
dl_patch[].language.name | Patch language name.
dl_patch[].version | Patch version string.
dl_patch[].total_size | Total size in bytes.
dl_patch[].files[] | Files that make up the patch.
dl_patch[].files[].id | File ID.
dl_patch[].files[].size | File size in bytes.
dl_patch[].files[].downlink | Download API URL of the file.
dl_langpack[] | Downloadable language packs. Only 1 product has one.
dl_langpack[].id | Language pack ID.
dl_langpack[].name | Language pack name.
dl_langpack[].os | Operating system of the language pack.
dl_langpack[].language.code | Language code.
dl_langpack[].language.name | Language name.
dl_langpack[].version | Version string.
dl_langpack[].total_size | Total size in bytes.
dl_langpack[].files[] | Files that make up the language pack.
dl_langpack[].files[].id | File ID.
dl_langpack[].files[].size | File size in bytes.
dl_langpack[].files[].downlink | Download API URL of the file.
dl_bonus[] | Bonus content (manuals, soundtracks, wallpapers).
dl_bonus[].id | Bonus ID.
dl_bonus[].name | Bonus name.
dl_bonus[].bonus_type | Bonus category, e.g. guides & reference.
dl_bonus[].count | Number of items in the bonus.
dl_bonus[].total_size | Total size in bytes.
dl_bonus[].files[] | Files that make up the bonus.
dl_bonus[].files[].id | File ID.
dl_bonus[].files[].size | File size in bytes.
dl_bonus[].files[].downlink | Download API URL of the file.
screenshots | List of screenshot image hashes.
videos[] | Store videos.
videos[].provider | Video host, e.g. youtube.
videos[].video_url | Embed URL of the video.
videos[].thumbnail_url | Thumbnail image URL.
image_background | Image hash of the store background.
image_boxart | Image hash of the box art.
image_galaxy_background | Image hash of the Galaxy client background.
image_icon | Image hash of the icon.
image_icon_square | Image hash of the square icon.
image_logo | Image hash of the logo.
link_store | URL of the GOG store page.
link_forum | URL of the GOG forum.
link_support | URL of the GOG support page.

## prices.json / prices_pre2019.json

Price history, nested as `{country: {currency: [price entries]}}`. `prices_pre2019.json` holds the older history in the same shape.

- **US / USD only.** Both files contain a single country (US) and currency (USD).
- **Two separate date ranges with a gap.** `prices_pre2019.json` covers Jun 2017 – Oct 2018 (33,984 entries). `prices.json` covers Apr 2021 – Oct 2026 (1,036,454 entries). No prices were recorded between Oct 2018 and Apr 2021, although product and change tracking continued.
- **Null prices.** 2,998 entries in `prices.json` and 3,104 in `prices_pre2019.json` have null `price_base` and `price_final`.
- **Analysis scope.** Price analysis uses `prices.json` only. The pre-2019 archive is excluded because of the gap and sparse coverage.

column | description
-------|---------
country (key) | Country code of the store region, e.g. US.
currency (key) | Currency code, e.g. USD.
currency | Currency code (repeated inside each entry).
date | Timestamp the price was recorded (UTC, ISO 8601).
price_base | Regular price. Appears to be in cents (999 = $9.99).
price_final | Price actually charged, after any discount. Same units as price_base.

## changes.json

List of change events GOG DB recorded for the product.

column | description
-------|---------
product_id | Product the change belongs to.
timestamp | Timestamp of the change (UTC, ISO 8601).
category | Area that changed: product, download, build or property.
action | Type of change: add, change or del.
build_id | Build ID for build changes. Null otherwise.
download_record | Details of a download change. Null when category is not download.
download_record.dl_type | Download type: installer, patch, langpack or bonus.
download_record.dl_old_software | Installer/patch/langpack before the change. Null for adds and for bonus changes.
download_record.dl_new_software | Installer/patch/langpack after the change. Null for deletes and for bonus changes.
download_record.dl_old_software.id / dl_new_software.id | Download ID, e.g. installer_windows_en.
download_record.dl_old_software.name / dl_new_software.name | Download name.
download_record.dl_old_software.os / dl_new_software.os | Operating system of the download.
download_record.dl_old_software.language.code / dl_new_software.language.code | Language code.
download_record.dl_old_software.language.name / dl_new_software.language.name | Language name.
download_record.dl_old_software.version / dl_new_software.version | Version string.
download_record.dl_old_software.total_size / dl_new_software.total_size | Total size in bytes.
download_record.dl_old_software.files / dl_new_software.files | File list. Always null in changes.json.
download_record.dl_old_bonus | Bonus item before the change. Null for adds and for software changes.
download_record.dl_new_bonus | Bonus item after the change. Null for deletes and for software changes.
download_record.dl_old_bonus.id / dl_new_bonus.id | Bonus ID.
download_record.dl_old_bonus.name / dl_new_bonus.name | Bonus name.
download_record.dl_old_bonus.bonus_type / dl_new_bonus.bonus_type | Bonus category.
download_record.dl_old_bonus.count / dl_new_bonus.count | Number of items in the bonus.
download_record.dl_old_bonus.total_size / dl_new_bonus.total_size | Total size in bytes.
download_record.dl_old_bonus.files / dl_new_bonus.files | File list. Always null in changes.json.
property_record | Details of a property change. Null when category is not property.
property_record.property_name | Name of the product.json field that changed, e.g. comp_systems.
property_record.value_old | Value before the change. Type depends on the field: text, true/false, or a list of text.
property_record.value_new | Value after the change. Same type as value_old.

## builds/<build_id>.json

Full Galaxy build manifest, one file per build (71,948 files). The file name matches `builds[].id` in product.json.
There are two different layouts, depending on `builds[].generation` in product.json:

- **Generation 1** (`version` = 1, 2,787 files): everything is nested under `product`.
- **Generation 2** (`version` = 2, 69,161 files): fields are at the top level and there is no `product` key.

### Shared

column | description
-------|---------
version | Manifest layout version: 1 = generation 1, 2 = generation 2.

### Generation 1 (`version` = 1)

column | description
-------|---------
product.timestamp | Build timestamp. Matches legacy_build_id in product.json.
product.projectName | Project name of the build.
product.installDirectory | Default install folder name.
product.rootGameID | Product ID of the main game.
product.disableSync | True if cloud sync is disabled. Rarely present.
product.gameIDs[] | Games included in the build.
product.gameIDs[].gameID | Product ID of the game.
product.gameIDs[].name.en | English name of the game.
product.gameIDs[].standalone | True if the game can be installed on its own.
product.gameIDs[].dependencies[] | Product IDs this game depends on.
product.depots[] | Content chunks that make up the build.
product.depots[].gameIDs[] | Product IDs the depot belongs to.
product.depots[].languages[] | Languages of the depot (Neutral = all languages).
product.depots[].systems[] | Operating systems of the depot, e.g. Windows.
product.depots[].size | Depot size in bytes, stored as text.
product.depots[].manifest | File name of the depot manifest.
product.depots[].redist | Name of a redistributable this depot installs, e.g. DirectX, DOSBox074, MSVC2010. Only on redist depots.
product.depots[].executable | Installer executable of the redistributable. Only on redist depots.
product.depots[].argument | Command-line arguments for the redistributable installer. Only on redist depots.
product.depots[].targetDir | Folder the depot installs into, e.g. DOSBOX. Rarely present.
product.support_commands[] | Helper executables run on install.
product.support_commands[].executable | Path to the helper executable.
product.support_commands[].argument | Command-line arguments.
product.support_commands[].gameID | Product ID the command belongs to.
product.support_commands[].languages[] | Languages the command applies to.
product.support_commands[].systems[] | Operating systems the command applies to.

### Generation 2 (`version` = 2)

column | description
-------|---------
baseProductId | Product ID of the main game.
buildId | Build ID, as text.
platform | Operating system of the build: windows or osx.
installDirectory | Default install folder name.
clientId | Galaxy API client ID of the game.
clientSecret | Galaxy API client secret of the game. Published in the manifest, not a private credential, but no reason to copy it into analysis tables.
scriptInterpreter | True if the build uses GOG's script interpreter installer.
tags[] | Build tags, e.g. galaxy, editor_v_1_5_0.
dependencies[] | Redistributables the build needs, e.g. DirectX, MSVC2017_x64.
cloudSaves[] | Cloud save folders.
cloudSaves[].name | Save slot name, e.g. saves.
cloudSaves[].location | Save folder path with placeholders, e.g. `<?DOCUMENTS?>/...`.
products[] | Products (game plus DLCs) included in the build.
products[].productId | Product ID.
products[].name | Product name.
products[].script | Installer script name. Rarely present.
products[].temp_executable | Helper executable run on install. Often empty text.
products[].temp_arguments | Arguments for temp_executable. Often empty text.
depots[] | Content chunks that make up the build.
depots[].productId | Product ID the depot belongs to.
depots[].languages[] | Languages of the depot (* = all languages).
depots[].manifest | Manifest hash of the depot.
depots[].size | Unpacked size in bytes.
depots[].compressedSize | Download (compressed) size in bytes.
depots[].isGogDepot | True if the depot is GOG-added content (e.g. Galaxy integration files).
depots[].osBitness[] | CPU bitness the depot is for: 32, 64, or !32 / !64 meaning "not".
depots[].os[] | Operating systems the depot is for. Rarely present.
offlineDepot | The depot used for offline installers.
offlineDepot.productId | Product ID of the offline depot.
offlineDepot.languages[] | Languages of the offline depot.
offlineDepot.manifest | Manifest hash of the offline depot.
offlineDepot.size | Unpacked size in bytes.
offlineDepot.compressedSize | Download (compressed) size in bytes.
offlineDepot.isGogDepot | True if the offline depot is GOG-added content.
