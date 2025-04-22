social-media-analytics/  
├── config/  
│   ├── cluster.properties      # Cluster configuration settings  
│   ├── hot_content.txt         # Hot content thresholds/rules  
│   └── threshold.txt           # Threshold configurations  
│  
├── docs/  
│   └── join_strategy.md        # Documentation on data joining strategies  
│  
├── input/  
│   ├── social_media_logs.txt   # Raw social media log data  
│   └── user_profiles.txt       # User profile data  
│  
├── output/                     # Processed/generated outputs  
│  
├── scripts/  
│   ├── partitioner.sh          # Script for data partitioning  
│   └── threshold_calculator.sh # Script for threshold calculations  
│  
├── src/  
│   ├── actions/                # User action processing  
│   │   ├── actions_combiner.py # Combines mapped actions  
│   │   ├── actions_mapper.py   # Maps user actions  
│   │   └── actions_reducer.py  # Reduces action data  
│   │  
│   ├── cleaner/                # Data cleaning/transformation  
│   │   ├── cleaner_mapper.py   # Maps raw data for cleaning  
│   │   └── cleaner_reducer.py  # Reduces cleaned data  
│   │  
│   ├── common/                 # Shared utilities  
│   │   └── utils.py            # Helper functions (e.g., I/O, logging)  
│   │  
│   ├── join/                   # Data joining operations  
│   │   ├── join_mapper.py      # Maps data for joins  
│   │   └── join_reducer.py     # Reduces joined datasets  
│   │  
│   ├── threshold/              # Threshold-based filtering  
│   │   ├── threshold_mapper.py # Maps threshold checks  
│   │   └── threshold_reducer.py# Aggregates threshold results  
│   │  
│   └── trending/               # Trending content analysis  
│       ├── trending_mapper.py  # Maps content for trend detection  
│       └── trending_reducer.py # Reduces trending results  
│  
├── run_pipeline.sh             # Main pipeline execution script  
├── threshold_mapper.py         # (Global) MapReduce mapper for thresholds  
└── threshold_reducer.py        # (Global) MapReduce reducer for thresholds  
