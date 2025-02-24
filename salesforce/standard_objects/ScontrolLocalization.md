#### ScontrolLocalization

The translated value of the field label for an s-control.

Important: Visualforce pages supersede s-controls. Organizations that haven’t previously used s-controls can’t create them.
Existing s-controls are unaffected, and can still be edited.

When the Translation Workbench is enabled for your organization, provides the translation of the field label of an s-control.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
**•** Your organization must be using Professional, Enterprise, Developer, or Unlimited Edition and be enabled for the Translation
Workbench.

**•** To view this object, you must have the “View Setup and Configuration” permission.

##### Fields

```
LanguageLocaleKey
Language

```

**Type**
picklist

**Properties**
Create,

Filter,

Nillable, Restricted picklist

**Description**

This field is available in API version 16.0 and earlier. It is the same as the Language
field.

**Type**
picklist


-----

**Properties**
Create, Filter, Nillable, Restricted picklist

**Description**

This field is available in API version 17.0 and later. The combined language and locale
ISO code, which controls the language for labels displayed in an application.

This picklist contains the following fully-supported languages:

**•** Chinese (Simplified): `zh_CN`

**•** Chinese (Traditional): `zh_TW`

**•** Danish: `da`

**•** Dutch: `nl_NL`

**•** English: `en_US`

**•** Finnish: `fi`

**•** French: `fr`

**•** German: `de`

**•** Italian: `it`

**•** Japanese: `ja`

**•** Korean: `ko`

**•** Norwegian: `no`

**•** Portuguese (Brazil): `pt_BR`

**•** Russian: `ru`

**•** Spanish: `es`

**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for
customer-defined translations.

**•** Swedish: `sv`

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is in
English.

The following end-user only languages are available.

**•** Arabic: `ar`

**•** Bulgarian: `bg`

**•** Croatian: `hr`

**•** Czech: `cs`

**•** English (UK): `en_GB`

**•** Greek: `el`

**•** Hebrew: `iw`

**•** Hungarian: `hu`

**•** Indonesian: `in`

**•** Polish: `pl`

**•** Portuguese (European): `pt_PT`


-----

**•** Romanian: `ro`

**•** Slovak: `sk`

**•** Slovenian: `sl`

**•** Turkish: `tr`

**•** Ukrainian: `uk`

**•** Vietnamese: `vi`

The following platform languages are available for organizations that use Salesforce
exclusively as a platform.

**•** Albanian: `sq`

**•** Afrikaans: `af`

**•** Amharic: `am`

**•** Arabic (Algeria): `ar_DZ`

**•** Arabic (Bahrain): `ar_BH`

**•** Arabic (Egypt): `ar_EG`

**•** Arabic (Iraq): `ar_IQ`

**•** Arabic (Jordan): `ar_JO`

**•** Arabic (Kuwait): `ar_KW`

**•** Arabic (Lebanon): `ar_LB`

**•** Arabic (Libya): `ar_LY`

**•** Arabic (Morocco): `ar_MA`

**•** Arabic (Oman): `ar_OM`

**•** Arabic (Qatar): `ar_QA`

**•** Arabic (Saudi Arabia): `ar_SA`

**•** Arabic (Sudan): `ar_SD`

**•** Arabic (Syria): `ar_SY`

**•** Arabic (Tunisia): `ar_TN`

**•** Arabic (United Arab Emirates): `ar_AE`

**•** Arabic (Yemen): `ar_YE`

**•** Armenian: `hy`

**•** Basque: `eu`

**•** Bosnian: `bs`

**•** Bengali: `bn`

**•** Burmese: `my`

**•** Catalan: `ca`

**•** Chinese (Hong Kong): `zh_HK`

**•** Chinese (Singapore): `zh_SG`

**•** Chinese (Malaysia): `zh_MY`

**•** Dutch (Belgium): `nl_BE`


-----

**•** English (Australia): `en_AU`

**•** English (Belgium): `en_BE`

**•** English (Canada): `en_CA`

**•** English (Cyprus): `en_CY`

**•** English (Germany): `en_DE`

**•** English (Hong Kong): `en_HK`

**•** English (India): `en_IN`

**•** English (Ireland): `en_IE`

**•** English (Israel): `en_IL`

**•** English (Malaysia): `en_MY`

**•** English (Malta): `en_MT`

**•** English (Netherlands): `en_NL`

**•** English (New Zealand): `en_NZ`

**•** English (Philippines): `en_PH`

**•** English (Singapore): `en_SG`

**•** English (South Africa): `en_ZA`

**•** English (United Arab Emirates): `en_AE`

**•** Estonian: `et`

**•** Farsi: `fa`

**•** French (Belgium): `fr_BE`

**•** French (Canada): `fr_CA`

**•** French (Luxembourg): `fr_LU`

**•** French (Morocco): `fr_MA`

**•** French (Switzerland): `fr_CH`

**•** Georgian: `ka`

**•** German (Austria): `de_AT`

**•** German (Belgium): `de_BE`

**•** German (Luxembourg): `de_LU`

**•** German (Switzerland): `de_CH`

**•** Greek (Cyprus): `el_CY`

**•** Greenlandic: `kl`

**•** Gujarati: `gu`

**•** Hawaiian: `haw`

**•** Haitian Creole: `ht`

**•** Hindi: `hi`

**•** Icelandic: `is`

**•** Irish: `ga`

**•** Italian (Switzerland): `it_CH`


-----

**•** Kannada: `kn`

**•** Kazakh: `kk`

**•** Khmer: `km`

**•** Latvian: `lv`

**•** Lithuanian: `lt`

**•** Luxembourgish: `lb`

**•** Macedonian: `mk`

**•** Malay: `ms`

**•** Malayalam: `ml`

**•** Maltese: `mt`

**•** Marathi: `mr`

**•** Montenegrin: `sh_ME`

**•** Romanian (Moldova): `ro_MD`

**•** Romansh: `rm`

**•** Russian (Armenia): `ru_AM`

**•** Russian (Belarus): `ru_BY`

**•** Russian (Kazakhstan): `ru_KZ`

**•** Russian (Kyrgyzstan): `ru_KG`

**•** Russian (Lithuania): `ru_LT`

**•** Russian (Moldova): `ru_MD`

**•** Russian (Poland): `ru_PL`

**•** Russian (Ukraine): `ru_UA`

**•** Samoan: `sm`

**•** Serbian (Cyrillic): `sr`

**•** Serbian (Latin): `sh`

**•** Spanish (Argentina): `es_AR`

**•** Spanish (Bolivia): `es_BO`

**•** Spanish (Chile): `es_CL`

**•** Spanish (Colombia): `es_CO`

**•** Spanish (Costa Rica): `es_CR`

**•** Spanish (Dominican Republic): `es_DO`

**•** Spanish (Ecuador): `es_EC`

**•** Spanish (El Salvador): `es_SV`

**•** Spanish (Guatemala): `es_GT`

**•** Spanish (Honduras): `es_HN`

**•** Spanish (Nicaragua): `es_NI`

**•** Spanish (Panama): `es_PA`

**•** Spanish (Paraguay): `es_PY`


-----

```
NamespacePrefix
ScontrolId

```


**•** Spanish (Peru): `es_PE`

**•** Spanish (Puerto Rico): `es_PR`

**•** Spanish (United States): `es_US`

**•** Spanish (Uruguay): `es_UY`

**•** Spanish (Venezuela): `es_VE`

**•** Swahili: `sw`

**•** Tagalog: `tl`

**•** Tamil: `ta`

**•** Te reo: `mi`

**•** Telugu: `te`

**•** Urdu: `ur`

**•** Welsh: `cy`

**•** Xhosa: `xh`

**•** Zulu: `zu`

The values in this field are not related to the default locale selection.

**Type**
string

**Properties**
Filter, Nillable

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org
that creates a managed package has a unique namespace prefix. Limit: 15 characters.
You can refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, NamespacePrefix is set to the namespace prefix
of the org for all objects that support it, unless an object is in an installed managed
package. In that case, the object has the namespace prefix of the installed
managed package. This field’s value is the namespace prefix of the Developer
Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only
for objects that are part of an installed managed package. All other objects have
no namespace prefix.

**Type**
reference

**Properties**
Create, Filter, Nillable

**Description**
The ID of the Scontrol that is being translated.


-----

```
 Value

##### Usage

```

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The actual translated field label of the s-control. Label is Translation.


Use this object to translate your s-controls into a supported language. Users with the Translation Workbench enabled can view s-control
translations, but either the “Customize Application” or “Manage Translation” permission is required to create or update s-control
translations.

SEE ALSO:

CategoryNodeLocalization

WebLinkLocalization
