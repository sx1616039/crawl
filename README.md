纪录片网络爬虫
-------

### 数据库 crawl ###

网站表  `website`

| 字段名              | 数据类型| 长度 | 说明       | 描述 |
|:-------------------|:-------|:----|:----------|:----|
|website_id|||| 网站id |
|web_name| | | | 网站名|
|domain|||| 域名 |
|part_num||||总纪录片部数|
|episode_num||||总纪录片集数|

类型表 `regular_type`

| 字段名              | 数据类型| 长度 | 说明       | 描述 |
|:-------------------|:-------|:----|:----------|:----|
|type_id||||id|
|type||||正则所属类型|
|description||||描述|

纪录片表 `documentary`

| 字段名              | 数据类型| 长度 | 说明       | 描述 |
|:-------------------|:-------|:----|:----------|:----|
|doc_name||||片名|
|episode_num||||集数|
|abstract||||简介|
|play_num||||总播放量|
|url||||纪录片url|
|total_length||||总片长 (单位秒)|
|institutions||||播出机构|
|release_time||||发布时间|
|cyclopedia_msg||||百度百科上的信息|
|website_id||||网站id|

爬取的url表 `urls`

| 字段名              | 数据类型| 长度 | 说明       | 描述 |
|:-------------------|:-------|:----|:----------|:----|
|url||||网址|
|depth||||层级|
|status||||状态（0 todo, 1 doing, 2 done, 3 exception）|
|description||||描述|
|website_id||||网站id|

正则表 `regexs`

| 字段名              | 数据类型| 长度 | 说明       | 描述 |
|:-------------------|:-------|:----|:----------|:----|
|website_id||||网站id|
|type_id|||| 类型id|
|regex|||| 正则 |

