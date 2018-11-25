# Documentation

  
### aggregate_numerical_features()

**Parameters:**

> **df**: *Pandas DataFrame, Default = None*  
> Dataset to join with.

> **attr**: *String,  Default = None*  
> Attribute to aggregate on.

**Returns:**

> **agg_df**: *Pandas DataFrame, Default = None*   
> The aggregated dataframe with the aggregated values mean, max, min, median, count, sum for each unique attribute.

```
Example:
```

### aggregate_categorical_features()

**Parameters:**

> **df**: *Pandas DataFrame, Default = None*    
> Dataset to join with.

> **attr**: *String,  Default = None*  
> Attribute to aggregate on.

**Returns:**

> **agg_df**: *Pandas DataFrame, Default = None*    
> The aggregated dataframe with the aggregated values mean, max, min, median, count, sum for each unique attribute.

```
Example:
```


### check_missing_data()

**Parameters:**

> **df**: *Pandas DataFrame, Default = None*    
> Dataset to check


**Returns:**

> **missing_df**: *Pandas DataFrame, Default = None*   
> Dataframe with two columns, number of missing data in each feature and percentage missing per feature.

```
Example:
```

# Install

`git clone
