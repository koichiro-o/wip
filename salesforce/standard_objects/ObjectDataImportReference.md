#### ObjectDataImportReference

Represents the relationships to the associated reference objects showing the source from which the data is imported. This object is
available in API version 57.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
ObjectDataImportReference is read only and can only be queried.


-----

##### Fields

**Field**
```
ObjectDataImportId
ObjectDataImportReferenceNumber

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Foreign key to the ObjectDataImport object.

This field is a relationship field.

**Relationship Name**
ObjectDataImport

**Relationship Type**
Lookup

**Refers To**
ObjectDataImport

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Foreign key to the reference object. For example, AsyncApiJob or DatasetImportRequest.

