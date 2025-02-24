#### ProductCategoryDataTranslation

Represents the translated values for the data stored within a ProductCategory record’s fields. This object is available in API version 46.0
and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
**•** Your organization must be using Enterprise, Performance, Unlimited, or Developer edition.

**•** Translation Workbench and data translation must be enabled in your org.

**•** To view this object, you must have the “View Setup and Configuration” permission

##### Fields

```
Description
IsOutOfDate

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The translated value for the Product Category description.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
Language
Name
ParentId

##### Usage

```

**Description**
Indicates whether the translation is out-of-date (true) or current (false). A translation
is out-of-date if the parent ProductCategory record is updated after the last translation was
filed.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language for these translated values.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The translated value for the Product Category name.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the category being translated.


Use this object to translate the data stored in a Product Category record into the different languages supported by Salesforce. If data
translation is enabled for custom fields on the ProductCategory object, additional ProductCategoryDataTranslation fields exist for
translating the data contained within those fields.
