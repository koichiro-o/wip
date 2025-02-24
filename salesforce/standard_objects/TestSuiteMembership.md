#### TestSuiteMembership

Associates an Apex class with an ApexTestSuite. This object is available in API version 36.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
In API version 49.0 and later, users must have the View Setup and Configuration permission to access this object.


-----

##### Fields

**Field Name**
```
ApexClassId
ApexTestSuiteId

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The Apex class whose tests are to be executed.

This is a relationship field.

**Relationship Name**
ApexClass

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The test suite to which the Apex class is assigned.

This is a relationship field.

**Relationship Name**
ApexTestSuite

**Relationship Type**
Lookup

**Refers To**
ApexTestSuite


Insert a TestSuiteMembership object using an API call to associate an Apex class with an ApexTestSuite object. (ApexTestSuite and
TestSuiteMembership aren’t editable through Apex DML.) To remove the class from the test suite, delete the TestSuiteMembership
object. If you delete an Apex test class or test suite, all TestSuiteMembership objects that contain that class or suite are deleted.


-----

The following SOQL query returns the membership object that relates this Apex class to this test suite.
```
SELECT Id FROM TestSuiteMembership WHERE ApexClassId = '01pD0000000Fhy9IAC'
   AND ApexTestSuiteId = '05FD00000004CDBMA2'

```
SEE ALSO:

ApexTestSuite
