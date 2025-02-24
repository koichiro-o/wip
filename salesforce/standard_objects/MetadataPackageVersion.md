#### MetadataPackageVersion

```
SELECT Name, NamespacePrefix FROM
MetadataPackage WHERE NamespacePrefix <>
''

```

Represents a package version (managed or unmanaged) that has been uploaded from the org you’re logged in to.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
BuildNumber

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The build number of the version. For example, if you upload two beta versions,
they have build numbers 1 and 2. Then, when you upload a non-beta version,


-----

```
IsDeprecated
MajorVersion
MetadataPackageId
MinorVersion
Name

```

the build number is 3. When you upload a new version, the build number resets
to 1.

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
Indicates whether the package version is deprecated. Available in API version
46.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first number in a package version number. A version number either has an
`x.y` format or an `x.y.z` format. The `x` represents the major version, `y the`
minor version, and `z` the patch version.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character package ID starting with `033.`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The second number in a package version number. A version number either has
an `x.y` format or an `x.y.z` format. The `x` represents the major version, `y`
the minor version, and `z` the patch version.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

The name of the package version.


-----

```
PatchVersion
ReleaseState

##### Usage

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The third number in a package version number, if present. A version number
either has an `x.y` format or an `x.y.z` format. The `x` represents the major
version, `y the minor version, and` `z` the patch version.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
If the package version is a beta version, the value is `Beta. Otherwise, the value`
is `Released.`


Here are examples of the types of API queries you can perform.

**Query** **String**

Get all package versions for the package that has a `SELECT Id, Name, ReleaseState,`
`MetadataPackageID` of 033D00000001xQlIAI `MajorVersion, MinorVersion, PatchVersion`
```
                          FROM MetadataPackageVersion WHERE
                          MetadataPackageId = '033D00000001xQlIAI'

```

Get the package version for the package with a specific
`MetadataPackageID` and a major version greater than 1

Get released package versions for the package with a specific
```
MetadataPackageID

```
**Java Code Sample**

```
SELECT Id FROM MetadataPackageVersion WHERE
MetadataPackageId ='033D00000001xQlIAI'
AND MajorVersion > 1
SELECT Id FROM MetadataPackageVersion WHERE
MetadataPackageId = '033D00000001xQlIAI'
AND ReleaseState = 'Released'

```

Suppose you want to push version 3.4.6 of your package to all orgs. Let’s write some code to identify the orgs eligible for the upgrade.
This example demonstrates how to generate the list of subscriber orgs eligible to be upgraded to version 3.4.6 of a package.

This code sample uses the Web Services Connector (WSC).


-----

**Next Step**

Create a push request using PackagePushRequest.
