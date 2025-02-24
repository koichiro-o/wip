#### ApexTypeImplementor

Represents Apex classes that directly or indirectly implement an interface. Using a SOQL query this object gets information about public
or global classes and only global classes for installed managed packages. This object is available in API version 54.0 and later.

##### Supported Calls
```
describeSObjects(), query()

 Fields

```
```
ApexClassId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The foreign key to the outer class that contains the Apex class implementing the interface.


-----

```
ClassName
ClassNamespacePrefix
DurableId
InterfaceApexClassId

```

This is a relationship field.

**Relationship Name**
ApexClass

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Apex class name that implements the interface. For an inner class that implements the
interface, the outer class and inner name separated by a period.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix of the class that implements the interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A unique identifier for the interface and implementor.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The foreign key to the outer class that contains the Apex class defining the interface. Null
for built-in system interfaces, such as `System.Batchable.`

This is a relationship field.

**Relationship Name**
InterfaceApexClass


-----

```
InterfaceName
InterfaceNamespacePrefix
IsConcrete

##### Usage

```

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The interface name for which Apex class implementation is retrieved. For an inner interface,
the outer Apex class name and the inner interface name separated by a period.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix of the class that defines the interface.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the implementing class is abstract (false) or not (true).


ApexTypeImplementor considers access modifiers based on the context, such as the namespace from which the ApexTypeImplementor
entity is queried. These are additional usage considerations.

**•** In installed managed packages, you get information about all global implementors in the org, and public implementors from the
managed package itself.

**•** ApexTypeImplementor appropriately filters classes that are annotated with `@Deprecated. For example it respects the package`
version dependency settings of a class when queried from that class.

**•** ApexTypeImplementor returns implementors where `ApexClass.IsValid` is set to `False (invalid classes) in addition to`
when it’s set to True. Classes that don’t compile or execute can be returned. An implementor class is only guaranteed to be usable
if `ApexClass.IsValid` is set to `True for the implementor.`

**•** If a package is installed but not yet compiled because Compile on Deploy is disabled, ApexTypeImplementor returns no values until
compilation is complete. In environments like sandboxes where Compile on Deploy can be disabled, you must perform a manual
compilation to get complete results.


-----
