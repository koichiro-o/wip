#### ProcessFlowMigration

Represents a process's migrated criteria and the resulting migrated flow. This object is available in API version 58.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
DeveloperName

```

**Type**
string

**Properties**
Filter, Group, Sort


-----

```
Language

```

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Lanaguage of the `MasterLabel.`

Possible values are:

**•** `af—Afrikaans`

**•** `am—Amharic`

**•** `ar—Arabic`

**•** `ar_AE—Arabic (United Arab Emirates)`

**•** `ar_BH—Arabic (Bahrain)`

**•** `ar_DZ—Arabic (Algeria)`

**•** `ar_EG—Arabic (Egypt)`

**•** `ar_IQ—Arabic (Iraq)`

**•** `ar_JO—Arabic (Jordan)`

**•** `ar_KW—Arabic (Kuwait)`

**•** `ar_LB—Arabic (Lebanon)`

**•** `ar_LY—Arabic (Libya)`

**•** `ar_MA—Arabic (Morocco)`

**•** `ar_OM—Arabic (Oman)`

**•** `ar_QA—Arabic (Qatar)`

**•** `ar_SA—Arabic (Saudi Arabia)`

**•** `ar_SD—Arabic (Sudan)`

**•** `ar_SY—Arabic (Syria)`

**•** `ar_TN—Arabic (Tunisia)`

**•** `ar_YE—Arabic (Yemen)`

**•** `bg—Bulgarian`

**•** `bn—Bengali`

**•** `bs—Bosnian`

**•** `ca—Catalan`

**•** `cs—Czech`

**•** `cy—Welsh`

**•** `da—Danish`


-----

**•** `de—German`

**•** `de_AT—German (Austria)`

**•** `de_BE—German (Belgium)`

**•** `de_CH—German (Switzerland)`

**•** `de_LU—German (Luxembourg)`

**•** `el—Greek`

**•** `el_CY—Greek (Cyprus)`

**•** `en_AE—English (United Arab Emirates)`

**•** `en_AU—English (Australian)`

**•** `en_BE—English (Belgium)`

**•** `en_CA—English (Canadian)`

**•** `en_CY—English (Cyprus)`

**•** `en_DE—English (Germany)`

**•** `en_GB—English (UK)`

**•** `en_HK—English (Hong Kong)`

**•** `en_IE—English (Ireland)`

**•** `en_IL—English (Israel)`

**•** `en_IN—English (Indian)`

**•** `en_MT—English (Malta)`

**•** `en_MY—English (Malaysian)`

**•** `en_NL—English (Netherlands)`

**•** `en_NZ—English (New Zealand)`

**•** `en_PH—English (Philippines)`

**•** `en_SG—English (Singapore)`

**•** `en_US—English`

**•** `en_ZA—English (South Africa)`

**•** `es—Spanish`

**•** `es_AR—Spanish (Argentina)`

**•** `es_BO—Spanish (Bolivia)`

**•** `es_CL—Spanish (Chile)`

**•** `es_CO—Spanish (Colombia)`

**•** `es_CR—Spanish (Costa Rica)`

**•** `es_DO—Spanish (Dominican Republic)`

**•** `es_EC—Spanish (Ecuador)`

**•** `es_GT—Spanish (Guatemala)`

**•** `es_HN—Spanish (Honduras)`

**•** `es_MX—Spanish (Mexico)`

**•** `es_NI—Spanish (Nicaragua)`


-----

**•** `es_PA—Spanish (Panama)`

**•** `es_PE—Spanish (Peru)`

**•** `es_PR—Spanish (Puerto Rico)`

**•** `es_PY—Spanish (Paraguay)`

**•** `es_SV—Spanish (El Salvador)`

**•** `es_US—Spanish (United States)`

**•** `es_UY—Spanish (Uruguay)`

**•** `es_VE—Spanish (Venezuela)`

**•** `et—Estonian`

**•** `eu—Basque`

**•** `fa—Farsi`

**•** `fi—Finnish`

**•** `fr—French`

**•** `fr_BE—French (Belgium)`

**•** `fr_CA—French (Canadian)`

**•** `fr_CH—French (Switzerland)`

**•** `fr_LU—French (Luxembourg)`

**•** `fr_MA—French (Morocco)`

**•** `ga—Irish`

**•** `gu—Gujarati`

**•** `haw—Hawaiian`

**•** `hi—Hindi`

**•** `hmn—Hmong`

**•** `hr—Croatian`

**•** `ht—Haitian Creole`

**•** `hu—Hungarian`

**•** `hy—Armenian`

**•** `in—Indonesian`

**•** `is—Icelandic`

**•** `it—Italian`

**•** `it_CH—Italian (Switzerland)`

**•** `iw—Hebrew`

**•** `ja—Japanese`

**•** `ji—Yiddish`

**•** `ka—Georgian`

**•** `kk—Kazakh`

**•** `kl—Greenlandic`

**•** `km—Khmer`


-----

**•** `kn—Kannada`

**•** `ko—Korean`

**•** `lb—Luxembourgish`

**•** `lt—Lithuanian`

**•** `lv—Latvian`

**•** `mi—Te reo`

**•** `mk—Macedonian`

**•** `ml—Malayalam`

**•** `mr—Marathi`

**•** `ms—Malay`

**•** `mt—Maltese`

**•** `my—Burmese`

**•** `nl_BE—Dutch (Belgium)`

**•** `nl_NL—Dutch`

**•** `no—Norwegian`

**•** `pa—Punjabi`

**•** `pl—Polish`

**•** `pt_BR—Portuguese (Brazil)`

**•** `pt_PT—Portuguese (European)`

**•** `rm—Romansh`

**•** `ro—Romanian`

**•** `ro_MD—Romanian (Moldova)`

**•** `ru—Russian`

**•** `ru_AM—Russian (Armenia)`

**•** `ru_BY—Russian (Belarus)`

**•** `ru_KG—Russian (Kyrgyzstan)`

**•** `ru_KZ—Russian (Kazakhstan)`

**•** `ru_LT—Russian (Lithuania)`

**•** `ru_MD—Russian (Moldova)`

**•** `ru_PL—Russian (Poland)`

**•** `ru_UA—Russian (Ukraine)`

**•** `sh—Serbian (Latin)`

**•** `sh_ME—Montenegrin`

**•** `sk—Slovak`

**•** `sl—Slovene`

**•** `sm—Samoan`

**•** `sq—Albanian`

**•** `sr—Serbian (Cyrillic)`


-----

```
MasterLabel
MigratedCriteriaLabel
MigratedCriteriaName

```


**•** `sv—Swedish`

**•** `sw—Swahili`

**•** `ta—Tamil`

**•** `te—Telugu`

**•** `th—Thai`

**•** `tl—Tagalog`

**•** `tr—Turkish`

**•** `uk—Ukrainian`

**•** `ur—Urdu`

**•** `vi—Vietnamese`

**•** `xh—Xhosa`

**•** `zh_CN—Chinese (Simplified)`

**•** `zh_HK—Chinese (Hong Kong)`

**•** `zh_MY—Chinese (Malaysia)`

**•** `zh_SG—Chinese (Singapore)`

**•** `zh_TW—Chinese (Traditional)`

**•** `zu—Zulu`

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for the ProcessFlowMigration.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the criteria that was migrated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the criteria that was migrated.


-----

```
NamespacePrefix
