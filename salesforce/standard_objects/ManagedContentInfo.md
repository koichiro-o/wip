#### ManagedContentInfo

Allows the creation of relationship to Product using ProductMedia. This object is available in API version 49.0 to 57.0. In API version 58.0
and later, use the ManagedContent object.


-----

##### Supported Calls
```
describeSObjects()

 Special Access Rules

```
You must have the B2B Commerce license and a CMS workspace to access a web store.

##### Usage

The CMS content import process returns a ManageContentInfo ID for each piece of content. The ManagedContentInfo entity has a 1:1
relationship with ProductMedia. To create this relationship, ProductMedia must be associated with a Product entity, for example, Product

- ProductMedia > ManagedContentInfo. Use the ID to associate content uploaded through the API with the ProductMedia entity
