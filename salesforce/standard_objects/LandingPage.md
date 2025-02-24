#### LandingPage

Represents an Account Engagement landing page. A landing page is a web page that a visitor reaches after clicking a link or advertisement.
Landing pages can be created in Account Engagement and synced to Salesforce or created on the Landing Page object in Account
Engagement Lightning App. This object is available in API version 42.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

To access this object, your org must use Account Engagement and users need the CRM User or Sales User permission set. To create,
update, or delete a builder landing page, the Use Account Engagement Content Experience permission set is required.

##### Fields

```
CampaignId
ContentLastSaved
ContentLastSavedById
FallbackUrl

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the related campaign.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The date and time of the last time someone changed and saved the landing page
Name, Campaign, Content, IsHideFromSearchEngineIndex, or Vanity URL fields.
This field is available in API version 53.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The user who last changed and saved the Content body. This is a relationship
field. This field is available in API version 53.0 and later.

**Relationship Name**

ContentLastSaved

**Relationship Type**

Lookup

**Refers To**

User

**Type**
string


-----

```
FooterCode
FormErrorRate
FormSubmissionRate
HeaderCode
IsHideFromSearchEngineIndex

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The URL used to redirect viewers after the landing page is unpublished. This field
is available in API version 54.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

`<Script>, <style>, and <link>` code added before the landing page’s
closing body tag. This field is available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Group, Sort

**Description**

The percentage of errors made on the landing page form. Calculated as total
errors divided by total views.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

The percentage of form submissions based on the total number of landing page
views.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

`<Script>, <style>, and <link>` code added to the head tag of the landing
page. This field is available in API version 54.0 and later.

**Type**
boolean


-----

```
LastPublished
LastPublishedById
LastReferencedDate
LastViewedDate

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the landing page is hidden from search engine indexing. The
default value is `false. This field is available in API version 53.0 and later.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The date and time of the last time someone published the landing page. This
field is available in API version 53.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The user who last published the landing page. This is a relationship field. This
field is available in API version 53.0 and later.

**Relationship Name**

LastPublished

**Relationship Type**

Lookup

**Refers To**

User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

Indicates when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
Name
PublicLink
Source
Status
TotalFormErrors

```

**Description**

The date and time when the current user last viewed this record. If this value is
null, this record might only have been referenced (see
```
  LastReferencedDate) and not viewed. This field is available in API version

```
53.0 and later.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The name of the landing page.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The URL where the landing page is available. This field is available in API version
53.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Indicates where the landing page was created. The default value is
```
  Salesforce. This field is available in API version 53.0 and later.

```
**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Indicates the state of the landing page: Draft, Published, or Published
```
  (Changes Pending). The default value is Draft. This field is available in

```
API version 53.0 and later.

**Type**
int


-----

```
TotalFormSubmissions
TotalTrackedLinkClicks
TotalViews
UniqueFormErrors
UniqueFormSubmissions

```

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of times a visitor or prospect enters an invalid email address
or leaves a required field blank on a landing page form.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of times a form on the landing page has been submitted.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of times prospects clicked a link on the landing page’s thank you
page.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of times visitors and prospects viewed your landing page. This
total includes multiple views from the same person.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of individual visitors and prospects who made an error on the form.
This metric doesn’t include multiple errors from the same person.

**Type**
int


-----

```
UniqueTrackedLinkClicks
UniqueViews
VanityUrl

##### Associated Objects

```

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of individual visitors who submitted a form on the landing page.
This metric doesn’t include multiple submissions from the same person.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of times a prospect clicked a link on the landing page’s thank you
page. This metric doesn’t include multiple clicks of the same link.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of individual visitors and prospects who viewed your landing page.
This metric doesn’t include multiple views from the same person.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The custom path that’s appended to tracker domains to create a vanity URL. This
field doesn’t support scheme or domain values. This field is available in API version
53.0 and later.


This object has the following associated objects. Unless otherwise noted, they’re available in the same API version as this object.

**LandingPageChangeEvent (API version 44.0)**
Change events are available for the object.

**LandingPageFeed**

Feed tracking is available for the object.


-----
