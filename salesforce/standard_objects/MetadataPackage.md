#### MetadataPackage

Represents a package that has been developed in the org you’re logged in to. Applies to unlocked, unmanaged, first-generation, and
second-generation managed packages.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
Name
NamespacePrefix
PackageCategory

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

The name of the package.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
For first-generation and second-generation managed packages, and unlocked
packages with namespaces, this field is the namespace prefix assigned to the
package. For unmanaged packages, or no-namespace unlocked packages, this
field is blank.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of package. Valid values are:


-----

**•** `Application` (internal use only)

**•** `Module` (internal use only)

**•** `Package—Represents either an unmanaged package or a first-generation`
managed package.

**•** `Package2—Represents either an unlocked package or a second-generation`
managed package.

The default value is Package.

This field is available in API version 49.0 and later.

##### Usage

Here are examples of the types of API queries you can perform.

**Query** **String**

Show all managed and unmanaged packages in the org `SELECT Name, NamespacePrefix FROM`
```
                          MetadataPackage

```

Show only managed packages in the org
