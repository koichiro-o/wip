#### SurveyResponse

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of the score calculated for a record. Possible values are:

**•** `Individual`

**•** `Overall`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier of the survey that contains the question for which scores are calculated.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the survey invitation for which scores are calculated.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier of the survey version for which scores are calculated.


Represents information about a participant’s response to a survey, such as the status of the response, the participant’s location, and
when the survey was completed.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete()

```
Note: You can’t define custom fields for the SurveyResponse object using the Object Manager.


-----

##### Fields

**Field Name**
```
CompletionDateTime
DataMapperExecutionStatus
InterviewGuid
InterviewId
InvitationId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the participant completed the survey.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of all the survey data maps after a response is received. This field is available
in API v49.0 and later, with Feedback Management - Starter and Feedback
Management - Growth licenses.

Possible values are:

**•** `Pending`

**•** `InProgress`

**•** `Success`

**•** `Error`

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable

**Description**
An automatically-generated, unique ID for a saved survey response.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the FlowInterview object that’s associated with this response.

**Type**
reference

**Properties**
Filter, Group, Sort


-----

```
IpAddress
Language

```

**Description**
The ID of the SurveyInvitation object that’s associated with this response.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the device the participant used to take the survey.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language that the participant used to complete the survey.

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


-----

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


-----

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


-----

```
LastReferencedDate

```


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
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
Latitude
Location
Longitude
Name
Status

```

**Description**
The date and time that another Salesforce object last referenced this
SurveyResponse object.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that someone last viewed this SurveyResponse object.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The latitude of the participant’s location.

**Type**
location

**Properties**
Nillable

**Description**
The latitude and longitude coordinates of the participant’s location.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The longitude of the participant’s location.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the participant.

**Type**
picklist


-----

```
SubmitterId
SurveyId
SurveyVersionId

```

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the survey. Possible values include:

**•** NotStarted — The participant hasn't opened the survey.

**•** Started — The participant has opened the survey.

**•** Paused — The participant has paused the survey. Paused isn't available for
invitations in which either
```
   OptionsAllowParticipantAccessTheirResponse or

```
`OptionsCollectAnonymousResponse` is true.

**•** PartiallyCompleted — The participant has partially completed the survey.
Available in API version 63.0 and later.

**•** Completed — The participant has completed the survey.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Salesforce user, contact, or lead who completed the survey.

**Relationship Name**
Submitter

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the survey that the participant completed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the version of the survey that the participant completed.


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyResponseChangeEvent on page 67**
Change events are available for the object.
