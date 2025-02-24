#### PromptVersion

```


**•** In orgs that aren't Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the in-app guidance.

**Type**
textarea

**Properties**
Create, Filter, Sort, Update

**Description**
The actual translated record details for the in-app guidance.


Represents an in-app guidance prompt or walkthrough. Available in API version 46.0 and later.

Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.
Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
[To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, see Considerations for](https://help.salesforce.com/s/articleView?id=sf.customhelp_lex_prompt_consider.htm&type=5&language=en_US)
[Creating In-App Guidance and Permissions for Creating and Accessing In-App Guidance in Salesforce Help for permissions.](https://help.salesforce.com/s/articleView?id=sf.customhelp_lex_prompt_consider.htm&type=5&language=en_US)

##### Prompts and Walkthroughs in Managed Packages

[For considerations about including in-app guidance in a managed package, see Guidelines for In-App Guidance in Managed Packages](https://help.salesforce.com/articleView?id=customhelp_iag_packages.htm&language=en_US)
in Salesforce Help.

[For more information about creating managed packages, see Create a First-Generation Managed Package.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/creating_packages.htm)


-----

[Unmanaged packages must contain a namespace prefix. For more information, see Register a Namespace for a First-Generation Managed](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)
[Packages and What happens to my namespace prefix when I install a package?.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)

##### Fields

```
ActionButtonLabel
ActionButtonLink
Body
DelayDays

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Label for the action button or link. Maximum of 25 characters. For a walkthrough, specify
this value on the last step.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
URL for the action button or link. Maximum of 1,000 characters. You can’t use the `GROUP`
`BY` option in a SOQL query for this field. For a walkthrough, specify this value on the last
step.

**Type**
textarea

**Properties**
Create, Update

**Description**
Body content.

In API version 60.0 and later, enter up to 4,000 characters for all prompt types.

In earlier API versions, enter up to 240 characters for floating prompts and targeted prompts.
Enter up to 4,000 characters for docked prompts.

For docked prompts, the maximum characters include HTML markup, not just readable text.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of days between occurrences. For a walkthrough, specify this value on the first step.


-----

```
Description
DismissButtonLabel
DisplayPosition
DisplayType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description. Maximum of 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Label for the dismiss button of a floating or targeted prompt. Maximum of 15 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The position of a floating prompt on the page. Valid values are:

**•** `TopLeft`

**•** `TopCenter`

**•** `TopRight`

**•** `MiddleLeft`

**•** `MiddleCenter`

**•** `MiddleRight`

**•** `BottomLeft`

**•** `BottomCenter`

**•** `BottomRight`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of prompt. Valid values are:

**•** `DockedComposer—A docked prompt`

**•** `FloatingPanel—A floating prompt`

**•** `Targeted—A targeted prompt. Available in API version 52.0 and later.`


-----

```
ElementRelativePosition
EndDate
Experience

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The location of a targeted prompt relative to the element. This field is available in API version
52.0 and later. Valid values are:

**•** `BottomCenter`

**•** `BottomLeft`

**•** `BottomRight`

**•** `LeftBottom`

**•** `LeftCenter`

**•** `LeftTop`

**•** `RightBottom`

**•** `RightCenter`

**•** `RightTop`

**•** `TopCenter`

**•** `TopLeft`

**•** `TopRight`

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date to stop showing the in-app guidance. For a walkthrough, specify this value on the
first step.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
This field corresponds to the Environment picklist in In-App Guidance Builder. Available in
version 60.0 and later.

Possible values are:

**•** `Lightning—Default. The in-app guidance is used in a Lightning Experience app or`
page.

**•** `Site—The in-app guidance is used in a supported Experience Cloud site page.`


-----

```
ExperienceContextId
Header
ImageAltText
ImageId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required if the value of Experience is Site. The ID of the Experience Cloud site context
associated with the in-app guidance prompt. Available in version 60.0 and later.

This field is a polymorphic relationship field.

**Relationship Name**
ExperienceContext

**Relationship Type**
Lookup

**Refers To**
Site

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Label for the header of a docked prompt. This value is the label contained in the window’s
browser bar. Maximum of 36 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the alt text of an image. Required if ImageLocation or ImageID is specified.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the ContentAsset that holds the image. Required if `ImageLocation` or
`ImageAltText` is specified.

This is a relationship field.

**Relationship Name**
Image


-----

```
ImageLocation
IndexWithIsPublished
IndexWithoutIsPublished
IsPublished
MasterLabel

```

**Relationship Type**
Lookup

**Refers To**
ContentAsset

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the location of the image in relation to the body text. Required if `ImageID` or
`ImageAltText` is specified. Valid values are:

**•** `Top`

**•** `Bottom`

**•** `Right, which is for floating or targeted prompts only`

**•** `Left, which is for floating or targeted prompts only`

**Type**
string

**Properties**
Filter, idLookup, Nillable, Sort

**Description**
Used by Salesforce for efficient querying.

**Type**
string

**Properties**
Filter, idLookup, Nillable, Sort

**Description**
Used by Salesforce for efficient querying.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the in-app guidance is active (true) or not (false).

**Type**
string


-----

```
ParentId
PublishedByUserId
PublishedDate

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label. Maximum of 80 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the in-app guidance.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Prompt

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the user who activated the in-app guidance. If the in-app guidance is part of a
package, this value is the user who installed the package.

This is a relationship field.

**Relationship Name**
PublishedByUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ReferenceElementContext
ShouldDisplayActionButton
ShouldIgnoreGlobalDelay
StartDate
StepNumber

```

**Description**
Indicates the date the in-app guidance was activated. If installed from a package, this value
is the date when the package was installed. For walkthroughs, this field can only be specified
on the first step.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Used by Salesforce to identify the element that the targeted prompt is associated with.
Available in API version 52.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether an action button or link is included (true) or not (false).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the in-app guidance ignores the global time delay and instead shows on
page load (true) or not (false). This field is available in API version 48.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the date to start showing the in-app guidance. For a walkthrough, specify this value
on the first step.

In API version 48.0 and earlier, this field is required.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
TargetAppDeveloperName
TargetAppNamespacePrefix
TargetPageKey1
TargetPageKey1Ref
TargetPageKey2

```

**Description**
Required for walkthroughs only. Indicates the number of the last step the user viewed or
interacted with in a walkthrough. Include up to 10 steps. Numbers must be consecutive
without repeated or skipped numbers. Available in API version 49.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The app’s developer name where the in-app guidance appears. Deprecated in API version
51.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The app’s namespace prefix where the in-app guidance appears. This value must match the
target app’s `NamespacePrefix` in the org that the package is being installed into.
Maximum of 15 characters. Deprecated in API version 51.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Used by Salesforce to identity the prompt’s page location along with
```
  targetPageKey2, targetPageKey3, targetPageKey4, and
  targetPageType.

```
**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Used by Salesforce to identify the prompt’s page location along with TargetPageKey2,
```
  TargetPageKey3, TargetPageKey4, and TargetPageType.

```
**Type**
string


-----

```
TargetPageKey3
TargetPageKey4
TargetPageType
TargetRecordType

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used by Salesforce to identify the prompt’s page location along with TargetPageKey1,
```
  TargetPageKey3, TargetPageKey4, and TargetPageType.

```
**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used by Salesforce to identify the prompt’s page location along with TargetPageKey1,
```
  TargetPageKey2, TargetPageKey4, and TargetPageType.

```
**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used by Salesforce to identify the page location along with `TargetPageKey1,`
```
  TargetPageKey2, TargetPageKey3, and TargetPageType. This field is available

```
in API version 53.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of page where the in-app guidance appears.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used by Salesforce to determine if in-app guidance is specific to a record type. This field is
available in API version 53.0 and later.

**Relationship Name**
TargetRecordType

**Relationship Type**
Lookup


-----

```
ThemeColor
ThemeSaturation
TimesToDisplay
Title

```

**Refers To**
RecordType

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates which custom theme color is applied to the in-app guidance. Required if
`ThemeSaturation` is specified. For a walkthrough, specify this value on the first step.
Valid values are:

**•** `Theme1—derived from the current brand color`

**•** `Theme2—derived from the current page background color`

**•** `Theme3—derived from the current global header color`

**•** `Theme4—derived from the current app theme color`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates which color value, or saturation, is applied to the in-app guidance that has a custom
theme color. Required if ThemeColor is specified. For a walkthrough, specify this value
on the first step. Valid values are:

**•** `Dark`

**•** `Light`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required if recurrences are scheduled. The maximum number of times to show the in-app
guidance. Salesforce detects whether the user interacts with the in-app guidance, then
determines whether to show the in-app guidance again or cancel scheduled recurrences.
Maximum value of 30. For a walkthrough, specify this value on the first step.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

```
UserAccess
UserProfileAccess
VersionNumber
VideoLink

```

**Description**
Required. The label for the title. Maximum of 36 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates which permissions can see the in-app guidance. Valid values are:

**•** `Everyone, which indicates that there’s no permission restrictions`

**•** `SpecificPermissions, which indicates that only users with all the specific user`
permissions specified can see the in-app guidance

In API version 48.0 and earlier, this field is required.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates which profiles can see the in-app guidance. This field is available in API version 48.0
and later. Valid values are:

**•** `Everyone, which indicates that there are no profile restrictions`

**•** `SpecificProfiles, which indicates that users with any of the specified user profiles`
can see the in-app guidance

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The number remains `1` since multiple versions aren’t saved in the org.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The embed URL for a video in a docked prompt. Maximum of 1,000 characters. You can
specify this field or the image field, but not both. This field is available in API version 48.0
[and later. See Considerations for Creating In-App Guidance.](https://help.salesforce.com/s/articleView?id=sf.customhelp_lex_prompt_consider.htm&language=en_US)


-----
