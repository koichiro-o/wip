#### UserProfile

Represents a Chatter user profile.

Note: This object has been deprecated as of API version 32.0. Use the User object to query information about a user in API version
32.0 and later.

##### Supported Calls
```
describeLayout(), query(), retrieve()

 Special Access Rules

```
**•** Information in hidden fields in a user's profile isn’t searchable by external users (with a portal profile) in an Experience Cloud site.
For example, if a user in a site has a hidden email address and an external user searches for it, the user record isn’t returned in the
search results. Hidden field values also aren’t returned when external users perform searches on nonhidden fields. So if an external
user searches for a user's name (can’t be hidden), any hidden field values associated with the user record such as a hidden email
address aren’t returned in the search results.

internal users belonging to the same Experience Cloud site can search for and view hidden field values in search results.

**•** Any fields that have been restricted in visibility will be returned empty, whether or not they are, and will not be removed from the
field listing.

##### Fields

```
AboutMe

```

**Type**
textarea


-----

`Address` (beta)
```
City
CompanyName
Country
Email

```

**Properties**
Filter, Nillable, Sort

**Description**
Information about the user, such as areas of interest or skills.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the address. Read-only. See Address
Compound Fields for details on compound address fields.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The city associated with the user profile.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The company associated with the user profile.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The country associated with the user profile.

**Type**
email

**Properties**
Filter, Group, idLookup, Sort

**Description**
The email address associated with the user profile.


-----

```
Fax
FirstName
FullPhotoUrl
IsActive
IsBadged

```

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The fax number associated with the user profile.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s first name.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the user's profile photo if Chatter is enabled.

The URL is updated every time a photo is uploaded and reflects the
most recent photo. If a newer photo is uploaded, the URL returned
for an older photo isn’t guaranteed to return a photo. Query this field
for the URL of the most recent photo.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user has access to log in (true) or not
(false). You can modify a User's active status from the user interface
or via the API.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user is visually badged (true) or not (false).
Users of the same Chatter user type (internal, external) are badged.
Different user types are not badged.


-----

```
LastName

```
`Latitude` (beta)

`Longitude` (beta)
```
ManagerId
MobilePhone

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The user’s last name.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with `Longitude` to specify the precise geolocation of an
address. Acceptable values are numbers between –90 and 90 up to
15 decimal places. For details on geolocation compound fields, see
Compound Field Considerations and Limitations

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with `Longitude` to specify the precise geolocation of an
address. Acceptable values are numbers between –90 and 90 up to
15 decimal places. For details on geolocation compound fields, see
Compound Field Considerations and Limitations

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who manages this user.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s mobile or cellular phone number.


-----

```
Name
Phone
PostalCode
SmallPhotoUrl
State
Street

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Concatenation of `FirstName` and `LastName.`

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s phone number.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s postal or ZIP code. Label is Zip/Postal Code.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for a thumbnail of the user's profile photo if Chatter is
enabled.

The URL is updated every time a photo is uploaded and reflects the
most recent photo. If a newer photo is uploaded, the URL returned
for an older photo isn’t guaranteed to return a photo. Query this field
for the URL of the most recent photo.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The state associated with the user profile.

**Type**
textarea


-----

```
Title
UserPreferencesActivityRemindersPopup
UserPreferencesApexPagesDeveloperMode
UserPreferencesDisableAllFeedsEmail
UserPreferencesDisableBookmarkEmail

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The street address associated with the user profile.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s business title, such as “Vice President.”

**Type**
boolean

**Properties**
Filter

**Description**
When `true, a reminder window automatically opens when an`
activity reminder is due. Corresponds to the `Trigger alert`
`when reminder comes due` checkbox at the Reminders
page in the personal settings in the user interface.

**Type**
boolean

**Properties**
Filter

**Description**
When `true, indicates that the user has enabled developer mode`
for editing Visualforce pages and controllers.

**Type**
boolean

**Properties**
Filter

**Description**
When `false, the user automatically receives email for all updates`
to Chatter feeds, based on the types of feed emails and digests the
user has enabled.

**Type**
boolean


-----

```
UserPreferencesDisableChangeCommentEmail
UserPreferencesDisableEndorsementEmail
UserPreferencesDisableFeedbackEmail
UserPreferencesDisableFileShareNotificationsForApi

```

**Properties**
Filter

**Description**
When `false, the user automatically receives email every time`
someone comments on a Chatter feed item after the user has
bookmarked it.

**Type**
boolean

**Properties**
Filter

**Description**
When `false, the user automatically receives email every time`
someone comments on a change the user has made, such as an
update to their profile.

**Type**
boolean

**Properties**
Filter

**Description**
When false, the member automatically receives email every time
someone endorses them for a topic.

**Type**
boolean

**Properties**
Filter

**Description**
When false, the user automatically receives emails related to WDC
feedback. This includes when someone requests or offers feedback,
shares feedback with the user, or reminds the user to answer a
feedback request.

**Type**
boolean

**Properties**
Filter

**Description**
When `false, email notifications are sent from the person who`
shared the file to the users that the file is shared with.


-----

```
UserPreferencesDisableFollowersEmail
UserPreferencesDisableLaterCommentEmail
UserPreferencesDisableLikeEmail
UserPreferencesDisableMentionsPostEmail
UserPreferencesDisableMessageEmail

```

**Type**
boolean

**Properties**
Filter

**Description**
When `false, the user automatically receives email every time`
someone starts following the user in Chatter.

**Type**
boolean

**Properties**
Filter

**Description**
When `false, the user automatically receives email every time`
someone comments on a feed item after the user has commented
on the feed item.

**Type**
boolean

**Properties**
Filter

**Description**
When `false, the user automatically receives email every time`
someone likes their post or comment.

**Type**
boolean

**Properties**
Filter

**Description**
When `false, the user automatically receives email every time`
they’re mentioned in posts.

**Type**
boolean

**Properties**
Filter

**Description**
When `false, the user automatically receives email for Chatter`
messages sent to the user.


-----

```
UserPreferencesDisableProfilePostEmail
UserPreferencesDisableRewardEmail
UserPreferencesDisableSharePostEmail
UserPreferencesDisableWorkEmail
UserPreferencesDisCommentAfterLikeEmail

```

**Type**
boolean

**Properties**
Filter

**Description**
When `false, the user automatically receives email every time`
someone posts to the user’s profile.

**Type**
boolean

**Properties**
Filter

**Description**
When false, the user automatically receives emails related to WDC
rewards. This includes when someone someone gives a reward to
the user.

**Type**
boolean

**Properties**
Filter

**Description**
When false, the user automatically receives email every time their
post is shared.

**Type**
boolean

**Properties**
Filter

**Description**
When `false, the user receives emails related to WDC feedback,`
goals, and coaching. The user must also sign up for individual emails
listed on the WDC email settings page. When `true, the user will`
not receive any emails related to WDC feedback, goals, or coaching
even if they are signed up for individual emails.

**Type**
boolean

**Properties**
Filter


-----

```
UserPreferencesDisMentionsCommentEmail
UserPreferencesDisProfPostCommentEmail
UserPreferencesEnableAutoSubForFeeds
UserPreferencesEventRemindersCheckboxDefault
UserPreferencesHideChatterOnboardingSplash

```

**Description**
When `false, the user automatically receives email every time`
someone comments on a post that the user liked.

**Type**
boolean

**Properties**
Filter

**Description**
When false, the user automatically receives email every time the
user is mentioned in comments.

**Type**
boolean

**Properties**
Filter

**Description**
When `false, the user automatically receives email every time`
someone comments on posts on the user’s profile.

**Type**
boolean

**Properties**
Filter

**Description**
When `true, the user automatically subscribes to feeds for any`
objects that the user creates.

**Type**
boolean

**Properties**
Filter

**Description**
When true, a reminder popup is automatically set on the user's
events. Corresponds to the `By default, set reminder`
`on Events to...` checkbox on the Reminders page in the
user interface. This field is related to UserPreference and customizing
activity reminders.

**Type**
boolean


-----

```
UserPreferencesHideCSNDesktopTask
UserPreferencesHideCSNGetChatterMobileTask
UserPreferencesHideS1BrowserUI
UserPreferencesHideSecondChatterOnboardingSplash

```

**Properties**
Filter

**Description**
When true, the initial Chatter onboarding prompts do not appear.

**Type**
boolean

**Properties**
Filter

**Description**
When `true, the Chatter recommendations panel never displays`
the recommendation to install Chatter Desktop.

**Type**
boolean

**Properties**
Filter

**Description**
When true, the Chatter recommendations panel never displays
the recommendation to install Chatter Mobile.

**Type**
boolean

**Properties**
Filter

**Description**
Controls the interface that the user sees when logging in to Salesforce
from a supported mobile browser. If false, the user is automatically
redirected to the Salesforce mobile web. If `true, the user sees the`
full Salesforce site. The default value is false. Label is Salesforce
**User.**

This field is available in API version 29.0 or later.

**Type**
boolean

**Properties**
Filter

**Description**
When `true, the secondary Chatter onboarding prompts do not`
appear.


-----

```
UserPreferencesReminderSoundOff
UserPreferencesShowCityToExternalUsers
UserPreferencesShowCityToGuestUsers

```

**Type**
boolean

**Properties**
Filter

**Description**
When true, a sound automatically plays when an activity reminder
is due. Corresponds to the `Play a reminder sound`
checkbox on the Reminders page in the user interface.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the city field in the user’s contact information.
City is visible only to internal members of the user’s organization
when:

**•** This field is `false. When` `false, this field returns the value`
```
   #N/A.

```
City is visible to external members in an Experience Cloud site when:

**•** This field is `true, or`

**•** This field is `false` but
```
   UserPreferencesShowCityToGuestUsers is true,

```
which overrides this field’s value.

External users are users with Community, Customer Portal, or partner
portal licenses.

The default value is false. This field is available in API version 26.0
and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the city field in the user’s contact information.
When `true, city is visible to guest users. Guest users can access`
public Site.com and Salesforce sites, and public pages in Experience
Cloud sites, via the Guest User license associated with each site. When
```
  false, this field returns the value #N/A.

```
When `true, this field overrides the value false` in
```
  UserPreferencesShowCityToExternalUsers, making

```
the user’s city visible to external members.


-----

```
UserPreferencesShowCountryToExternalUsers
UserPreferencesShowCountryToGuestUsers
UserPreferencesShowEmailToExternalUsers

```

The default value is false. This field is available in API version 28.0
and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the country field in the user’s contact
information. Country is visible only to internal members of the user’s
organization when:

**•** This field is `false. When` `false, this field returns the value`
```
   #N/A.

```
Country is visible to external members in an Experience Cloud site
when:

**•** This field is `true, or`

**•** This field is `false` but
```
   UserPreferencesShowCountryToGuestUsers is
   true, which overrides this field’s value.

```
External users are users with Community, Customer Portal, or partner
portal licenses.

The default value is false. This field is available in API version 26.0
and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the country field in the user’s contact
information. When `true, country is visible to guest users. Guest`
users can access public Site.com and Salesforce sites, and public
pages in Experience Cloud sites, via the Guest User license associated
with each site. When false, this field returns the value `#N/A.`

When `true, this field overrides the value false` in
```
  UserPreferencesShowCountryToExternalUsers,

```
making the user’s country visible to external members.

The default value is false. This field is available in API version 28.0
and later.

**Type**
boolean


-----

```
UserPreferencesShowFaxToExternalUsers
UserPreferencesShowManagerToExternalUsers
UserPreferencesShowMobilePhoneToExternalUsers

```

**Properties**
Filter

**Description**
Indicates the visibility of the email address field in the user’s contact
information. Email address is visible only to internal members of the
user’s organization when this field is false. Email address is visible
to external members in an Experience Cloud site when this field is
```
  true. External users are users with Community, Customer Portal,

```
or partner portal licenses.

When false, this field returns the value `#N/A. The default value`
is `false. This field is available in API version 26.0 and later.`

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the fax number field in the user’s contact
information. Fax number is visible only to internal members of the
user’s organization when this field is `false. Fax number is visible`
to external members in an Experience Cloud site when this field is
```
  true. External users are users with Community, Customer Portal,

```
or partner portal licenses.

When `false, this field returns the value #N/A. The default value`
is `false. This field is available in API version 26.0 and later.`

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the manager field in the user’s contact
information. Manager is visible only to internal members of the user’s
organization when this field is false. Manager is visible to external
members in an Experience Cloud site when this field is `true.`
External users are users with Community, Customer Portal, or partner
portal licenses.

When `false, this field returns the value #N/A. The default value`
is `false. This field is available in API version 26.0 and later.`

**Type**
boolean


-----

```
UserPreferencesShowPostalCodeToExternalUsers
UserPreferencesShowPostalCodeToGuestUsers

```

**Properties**
Filter

**Description**
Indicates the visibility of the mobile device number field in the user’s
contact information. The number is visible only to internal members
of the user’s organization when this field is `false. The number is`
visible to external members in an Experience Cloud site when this
field is `true. External users are users with Community, Customer`
Portal, or partner portal licenses.

When `false, this field returns the value #N/A. The default value`
is `false. This field is available in API version 26.0 and later.`

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the postal or ZIP code field in the user’s
contact information. Postal code is visible only to internal members
of the user’s organization when:

**•** This field is `false. When` `false, this field returns the value`
```
   #N/A.

```
Postal code is visible to external members in an Experience Cloud
site when:

**•** This field is `true, or`

**•** This field is `false` but
```
   UserPreferencesShowPostalCodeToGuestUsers

```
is `true, which overrides this field’s value.`

External users are users with Community, Customer Portal, or partner
portal licenses.

The default value is false. This field is available in API version 26.0
and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the postal or ZIP code field in the user’s
contact information. When `true, postal code is visible to guest`
users. Guest users can access public Site.com and Salesforce sites,
and public pages in Experience Cloud sites, via the Guest User license


-----

```
UserPreferencesShowProfilePicToGuestUsers
UserPreferencesShowStateToExternalUsers

```

associated with each site. When `false, this field returns the value`
```
  #N/A.

```
When `true, this field overrides the value false in`
```
  UserPreferencesShowPostalCodeToExternalUsers,

```
making the user’s postal code visible to external members.

The default value is false. This field is available in API version 28.0
and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the user’s profile photo. When true, the
photo is visible to guest users in an Experience Cloud site. Guest users
can access public Site.com and Salesforce sites, and public pages in
Experience Cloud sites, via the Guest User license associated with
each site.

When false, this field returns the stock photo. The default value
is false. This field is available in API version 28.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the state field in the user’s contact
information. State is visible only to internal members of the user’s
organization when:

**•** This field is `false. When` `false, this field returns the value`
```
   #N/A.

```
State is visible to external members in an Experience Cloud site when:

**•** This field is `true, or`

**•** This field is `false` but
```
   UserPreferencesShowStateToGuestUsers is
   true, which overrides this field’s value.

```
External users are users with Community, Customer Portal, or partner
portal licenses.

When `false, this field returns the value` `#N/A. The default value`
is `false. This field is available in API version 26.0 and later.`


-----

```
UserPreferencesShowStateToGuestUsers
UserPreferencesShowStreetAddressToExternalUsers
UserPreferencesShowTitleToExternalUsers

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the state field in the user’s contact
information. When true, state is visible to guest users. Guest users
can access public Site.com and Salesforce sites, and public pages in
Experience Cloud sites, via the Guest User license associated with
each site. When false, this field returns the value `#N/A.`

When `true, this field overrides the value false` in
UserPreferencesShowStateToExternalUsers, making the user’s state
visible to external members.

The default value is false. This field is available in API version 28.0
and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the street address field in the user’s contact
information. The address is visible only to internal members of the
user’s organization when this field is `false. The address is visible`
to external members in an Experience Cloud site when this field is
```
  true. External users are users with Community, Customer Portal,

```
or partner portal licenses.

When `false, this field returns the value #N/A. The default value`
is `false. This field is available in API version 26.0 and later.`

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the business title field in the user’s contact
information. Title is visible only to internal members of the user’s
organization when:

**•** This field is `false. When` `false, this field returns the value`
```
   #N/A.

```
Title is visible to external members in an Experience Cloud site when:

**•** This field is `true, or`


-----

```
UserPreferencesShowTitleToGuestUsers
UserPreferencesShowWorkPhoneToExternalUsers
UserPreferencesTaskRemindersCheckboxDefault

```


**•** This field is `false` but
```
   UserPreferencesShowTitleToGuestUsers is
   true, which overrides this field’s value.

```
External users are users with Community, Customer Portal, or partner
portal licenses.

The default value is `true. This field is available in API version 26.0`
and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the business title field in the user’s contact
information. When `true, title is visible to guest users. Guest users`
can access public Site.com and Salesforce sites, and public pages in
Experience Cloud sites, via the Guest User license associated with
each site. When false, this field returns the value `#N/A.`

When `true, this field overrides the value false` in
UserPreferencesShowTitleToExternalUsers, making the user’s title
visible to external members.

The default value is false. This field is available in API version 28.0
and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the work phone number field in the user’s
contact information. The number is visible only to internal members
of the user’s organization when this field is `false. The number is`
visible to external members in an Experience Cloud site when this
field is `true. External users are users with Community, Customer`
Portal, or partner portal licenses.

When `false, this field returns the value #N/A. The default value`
is `false. This field is available in API version 26.0 and later.`

**Type**
boolean

**Properties**
Filter


-----

**Description**
When true, a reminder popup is automatically set on the user's
tasks. Corresponds to the By default, set reminder on
`Tasks to...` checkbox on the Reminders page in the user
interface. This field is related to UserPreference and customizing
activity reminders.

##### Usage

Use this object to query Chatter—related information about the user. While the User object contains all the information about a user
and is historically tied to user management, UserProfile is a read-only entity that contains the information that is relevant in a Chatter
context.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**UserProfileFeed (API version 18.0–26.0)**
Feed tracking is available for the object.
