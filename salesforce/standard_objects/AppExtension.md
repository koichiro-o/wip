#### AppExtension

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the type of custom application. The value Aloha is for Salesforce
Classic, and `Lightning` is for Lightning Experience.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the utility bar associated with this application.


Represents a connection between the Field Service mobile app and another app, typically for passing record data to the Salesforce
mobile app or other apps. This object is available in API version 41.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
AppExtensionLabel

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The label in the UI for the app extension.


-----

```
AppExtensionName
FieldServiceMobileSettingsId
InstallationUrl
LaunchValue
ScopedToObjectTypes

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name of the app extension.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of a set of field service mobile settings.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL that takes the user to the app install location, such as the App Store or
Google Play.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A value directing the Field Service app to the appropriate app extension. The
Launch Value can be a static URL or a dynamic value that you can represent with
certain tokens. These tokens pass field information from the record that the user
is currently viewing. The basic format for these tokens is based on the field names;
for example: {!$Name}.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the types of records from which the app extension can be activated.
Scoping an app extension to an object lets users activate the app extension from
records of the specified type. For example, to scope to both work orders and


-----

```
Type

##### Associated Objects

```

service appointments you would use the value
```
  WorkOrder,ServiceAppointment.

```
**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A picklist of types of app extensions: iOS, Android, Flow, and Lightning Apps


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AppExtensionChangeEvent**

Change events are available for the object. Available in API version 55.0 and later.
