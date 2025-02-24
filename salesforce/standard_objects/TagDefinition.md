#### TagDefinition

```
Defines the attributes of child Tag objects.

##### Supported Calls


**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The developer name of the tab.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The name of the sObject corresponding to the tab.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The URL that can be used to launch this tab on desktop.

```
delete(), describeSObjects(), query(), retrieve(), search(), undelete(), update()

##### Special Access Rules

```
As of Summer ’20 and later, only authenticated internal and external users can access this object.

##### Fields

```
Name

```

**Type**
string


-----

```
Type

##### Usage

```

**Properties**
Filter, Nillable, Update

**Description**
Identifies the tag word or phrase.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Defines the visibility of a tag. Possible value are:

**•** **Public: The tag can be viewed and manipulated between all users in an organization.**

**•** **Personal: The tag can be viewed or manipulated only by a user with a matching**
```
   OwnerId.

```

When you create a tag for a record, an association is created with to a corresponding TagDefinition:

**•** If the value in the tag's `Name` field is new, a new TagDefinition record is automatically created and becomes the parent of the tag.

**•** If the value in the tag's Name field already exists in a TagDefinition, that TagDefinition automatically becomes the parent of the tag.

Each TagDefinition record has a one-to-many relationship with its child tag records.

The following standard objects represent tags for records:

**•** AccountTag

**•** AssetTag

**•** CampaignTag

**•** CaseTag

**•** ContactTag

**•** ContractTag

**•** DocumentTag

**•** EventTag

**•** LeadTag

**•** NoteTag

**•** OpportunityTag

**•** SolutionTag

**•** TaskTag

Custom objects may also be tagged. Tags for custom objects are identified by a suffix of two underscores immediately followed by the
word `tag. For example, a custom object named` `Meeting` has a corresponding tag named Meeting__tag in that organization’s
WSDL. Meeting__tag is only valid for `Meeting` objects.


-----

TagDefinition is useful for mass operations on any tag record. For instance, if you want to rename existing tags, you can search for the
appropriate TagDefinition object, update it, and the child tag's `Name` values are also changed. The following Java example replaces all
`WC` tags with the phrase `West Coast:`
```
public void tagDefinitionSample() {
  String soqlQuery = "SELECT Id, Name FROM TagDefinition " +
    "WHERE Name = 'WC'";
  QueryResult qResult = null;
  try {
    qResult = connection.query(soqlQuery);
   TagDefinition tagDef = (TagDefinition) qResult.getRecords()[0];
   tagDef.setName("West Coast");
   connection.update(new SObject[]{tagDef});
  } catch (ConnectionException ce) {
   ce.printStackTrace();
  }
}

```
When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.
