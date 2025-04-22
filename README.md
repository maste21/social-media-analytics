<img width="401" alt="image" src="https://github.com/user-attachments/assets/ed6450c6-1280-4738-b26f-90c00364d7ee" />


1. **Data Ingestion**: Raw logs (`social_media_logs.txt`) and profiles (`user_profiles.txt`)  
2. **Processing**:  
   - Data validation & cleansing  
   - User action aggregation  
   - Trending content identification  
   - Dataset joining  
3. **Output**: final reports 

## Quick Start

### Prerequisites
- Hadoop/Spark cluster or local MapReduce simulator
- Python 3.6+
- Bash shell

### Execution
1. **Configure cluster settings**:
   ```bash
   nano config/cluster.properties
Run the full pipeline:

bash
./run_pipeline.sh --input data/ --output output/

**Key Components**
**1. Data Cleansing**

Input: social_media_logs.txt

Output: Validated records in output/cleansed_data

Files:

src/cleaner/cleaner_mapper.py: Filters malformed records

src/cleaner/cleaner_reducer.py: Structures valid data

**2. Action Aggregation**

Metrics: Counts posts/likes/shares per user

Sorting: Descending by engagement

Files:

src/actions/actions_mapper.py: Counts actions

src/actions/actions_reducer.py: Ranks users

**3. Trending Detection**

Threshold: Configurable in config/hot_content.txt

Files:

src/trending/trending_mapper.py: Calculates engagement

src/trending/trending_reducer.py: Filters trending items

**4. Dataset Joining**

Strategy: Reduce-side join (documented in docs/join_strategy.md)

Files:

src/join/join_mapper.py: Tags records for joining

src/join/join_reducer.py: Merges datasets

Optimization Features
Data Skew Handling:

scripts/threshold_calculator.sh dynamically adjusts thresholds

src/join/join_reducer.py implements skew-resistant joins

**Performance:**

In-mapper combining in all mappers

Secondary sorting in reducers


**Troubleshooting**

**Common Issues:**

Input Path Errors: Verify paths in run_pipeline.sh

Permission Denied: Run chmod +x *.sh

Missing Dependencies: Install with pip install -r requirements.txt



### Key Features:
1. **Structure-First Approach**: Mirrors your actual repository layout
2. **MapReduce Focus**: Highlights the mapper/reducer pattern
3. **Cluster-Ready**: Includes Hadoop/Spark configuration notes
4. **Modular Documentation**: Links to component-specific docs

