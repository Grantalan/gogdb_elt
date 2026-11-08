# GOG DB Entity Relationship Diagram

How the JSON files break into tables once they're flattened. Wide nested parts (download file lists, depot details, cloud saves) are left out.

```mermaid
erDiagram
    PRODUCT ||--o{ PRICE : "price history"
    PRODUCT ||--o{ CHANGE : "change log"
    PRODUCT ||--o{ BUILD : "has builds"
    PRODUCT ||--o{ DOWNLOAD : "installers, patches, bonus"
    PRODUCT ||--o{ PRODUCT_TAG : "tagged"
    PRODUCT ||--o{ PRODUCT_LOCALIZATION : "languages"
    PRODUCT ||--o{ PRODUCT_LINK : "from"
    PRODUCT ||--o{ PRODUCT_LINK : "to"
    BUILD ||--o| BUILD_MANIFEST : "builds/<id>.json"
    BUILD ||--o{ CHANGE : "build changes"

    PRODUCT {
        int id PK
        string title
        string slug
        string type "game, dlc, pack"
        string store_state
        datetime global_date
        datetime store_date
        float user_rating
        int series_id
        string publisher
    }
    PRICE {
        int product_id FK
        datetime date
        string country "always US"
        string currency "always USD"
        int price_base "cents"
        int price_final "cents"
    }
    CHANGE {
        int product_id FK
        datetime timestamp
        string category "product, download, build, property"
        string action "add, change, del"
        int build_id FK "build changes only"
        string property_name "property changes only"
    }
    BUILD {
        int id PK
        int product_id FK
        int generation "1 or 2"
        string os
        string branch "null = main"
        string version
        datetime date_published
    }
    BUILD_MANIFEST {
        int build_id PK "FK to BUILD"
        int version "1 or 2"
        int base_product_id
        string platform
        string install_directory
    }
    DOWNLOAD {
        string id PK
        int product_id FK
        string dl_type "installer, patch, langpack, bonus"
        string os
        string language_code
        string version
        int total_size
    }
    PRODUCT_TAG {
        int product_id FK
        int tag_id
        string name
        int level "1 genre, 2 sub-genre"
    }
    PRODUCT_LOCALIZATION {
        int product_id FK
        string code
        bool text
        bool audio
    }
    PRODUCT_LINK {
        int from_product_id FK
        int to_product_id FK
        string link_type "dlc, edition, includes, requires"
    }
```

`PRODUCT_LINK` holds `dlcs`, `editions`, `includes_games` and `requires`. `is_included_in` and `required_by` are the same links read in reverse. `DOWNLOAD` holds the four `dl_*` arrays, with `dl_type` saying which one.

Column descriptions are in the [data dictionary](data_dictionary.md).
