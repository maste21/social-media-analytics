# Join Strategy Documentation

## Chosen Approach: Reduce-Side Join

### Advantages:
- Handles large datasets that don't fit in memory
- No requirement for sorted input files
- Naturally handles many-to-many relationships
- Works with any join key distribution

### Disadvantages:
- Higher network traffic due to shuffling all data
- Requires careful handling of data skew
- Potentially slower than map-side joins for small datasets

### Justification:
Given the requirements:
- User profiles may be large but likely smaller than activity data
- Activity data is already processed and sorted
- Need to handle potential skew in popular users
- No strict memory constraints specified

The reduce-side join provides the best balance of flexibility and scalability for this use case.