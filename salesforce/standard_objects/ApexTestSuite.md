#### ApexTestSuite

Represents a suite of Apex classes to include in a test run. A TestSuiteMembership object associates each class with the suite. This object
is available in API version 36.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
In API version 49.0 and later, users must have the View Setup and Configuration permission to access this object.

##### Fields

```
TestSuiteName

##### Usage

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Unique, Update

**Description**

The name of the Apex test suite. This label appears in the user interface.

This value is case-sensitive and must be unique.


Insert a TestSuiteMembership object using an API call to associate an Apex class with an ApexTestSuite object. (ApexTestSuite and
TestSuiteMembership aren’t editable through Apex DML.) To remove the class from the test suite, delete the TestSuiteMembership
object. If you delete an Apex test class or test suite, all TestSuiteMembership objects that contain that class or suite are deleted.

The following SOQL query returns the membership object that relates this Apex class to this test suite.
```
SELECT Id FROM TestSuiteMembership WHERE ApexClassId = '01pD0000000Fhy9IAC'
   AND ApexTestSuiteId = '05FD00000004CDBMA2'

```
SEE ALSO:

TestSuiteMembership
