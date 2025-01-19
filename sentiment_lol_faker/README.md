## data = '油管.xlsx'

  * 媒体ID  - post_id
  * 账号ID  - ID
  * 账号名  - username
  * 粉丝量  - followers
  * 标题  - title
  * 简介  - brief content
  * 发布时间  - post date and time
  * URL
  * 视频时长  - video duration
  * 观看量  - views
  * 点赞量  - likes
  * 评论量  - comments

## run data_process.ipynb will get the following dim/fact tables used in PowerBI

  | orignal_name | name_in_bi | 
  | :---:   | :---: |
  | data | fact_data |
  | id_dim | id_dim |
  | sentiment_data | sentiment_dim |
  | sentiment_dim | sentiment_desc_dim |
  | title_dim | title_dim |
  | words_dim | words_dim |


## process procedure

load data -> pre_process -> find korean language -> split data by language difference -> 
clean title and content (for sentiment) separatly -> sentiment score cannot get on korean language
-> translate korean part of data into english -> combine data together -> use nltk do tokenization for word and pos_tag analysis
-> use nltk get sentiment scores      
