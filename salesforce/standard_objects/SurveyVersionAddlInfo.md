#### SurveyVersionAddlInfo

Represents additional information about a survey version. This information defines the default settings of a survey version. This object
is available in API version 49.0 and later.


-----

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
EmailSender
EmailTemplateId
EngagementContextMetadata
InvitationSharingRole
Language

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
The organization-wide email address used to send a survey invitation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the email template that's used to send an automated survey invitation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The custom metadata created to get the engagement context from the participants.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the users that share edit access to a survey invitation.

Possible values are:

**•** `InvitationRecordCreator— Owner of the record that's associated with a`
survey invitation.

**•** `SurveyOwner`

**Type**
picklist


-----

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Language used to create the survey.

Possible values are:

**•** `af—Afrikaans`

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

**•** `de—German`

**•** `de_AT—German (Austria)`

**•** `de_BE—German (Belgium)`

**•** `de_CH—German (Switzerland)`

**•** `de_LU—German (Luxembourg)`

**•** `el—Greek`

**•** `en_AU—English (Australian)`


-----

**•** `en_CA—English (Canadian)`

**•** `en_GB—English (UK)`

**•** `en_HK—English (Hong Kong)`

**•** `en_IE—English (Ireland)`

**•** `en_IN—English (Indian)`

**•** `en_MY—English (Malaysian)`

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


-----

**•** `fr_CH—French (Switzerland)`

**•** `fr_LU—French (Luxembourg)`

**•** `ga—Irish`

**•** `gu—Gujarati`

**•** `hi—Hindi`

**•** `hr—Croatian`

**•** `hu—Hungarian`

**•** `hy—Armenian`

**•** `in—Indonesian`

**•** `is—Icelandic`

**•** `it—Italian`

**•** `it_CH—Italian (Switzerland)`

**•** `iw—Hebrew`

**•** `ja—Japanese`

**•** `ka—Georgian`

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

**•** `pl—Polish`

**•** `pt_BR—Portuguese (Brazil)`

**•** `pt_PT—Portuguese (European)`

**•** `rm—Romansh`

**•** `ro—Romanian`

**•** `ro_MD—Romanian (Moldova)`

**•** `ru—Russian`

**•** `sh—Serbian (Latin)`


-----

```
Name
SurveyQuestionId
SurveyVersionId

```


**•** `sh_ME—Montenegrin`

**•** `sk—Slovak`

**•** `sl—Slovene`

**•** `sq—Albanian`

**•** `sr—Serbian (Cyrillic)`

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

**•** `zh_SG—Chinese (Singapore)`

**•** `zh_TW—Chinese (Traditional)`

**•** `zu—Zulu`

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the survey question embedded in the email template used to send automated survey
invitations.

**Type**
reference


-----

**Properties**
Filter, Group, Sort

**Description**
ID of the survey version. This field is unique within your organization
