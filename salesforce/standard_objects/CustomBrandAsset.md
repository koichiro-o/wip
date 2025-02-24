#### CustomBrandAsset

Represents a branding element in a custom branding scheme. For example, a color, logo image, header image, or footer text. A
CustomBrandAsset can apply to an Experience Cloud site or to an org using the Salesforce mobile app. This object is available in API
version 28.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
This object is available only when your org has digital experiences enabled.

##### Fields

```
AssetCategory

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

Values include:

**•** `MotifZeronaryColor—The background color for the header. Label`
is `Zeronary motif color.`

If this CustomBrandAsset is for a network, this is the header color for the
network. If it is for an org, this is the header color when users access the
Salesforce mobile app.

**•** `MotifPrimaryColor—The color used for the active tab. Label is`
```
   Primary motif color.

```
Not used for the Salesforce mobile app branding.

**•** `MotifSecondaryColor—The color used for the top borders of lists`
and tables. Label is `Secondary motif color.`

Not used for the Salesforce mobile app branding.

**•** `MotifTertiaryColor—The background color for section headers on`
edit and detail pages. Label is `Tertiary motif color.`

Not used for the Salesforce mobile app branding.

**•** `MotifQuaternaryColor—If this CustomBrandAsset is for a network,`
this is the background color for network pages. If it is for an org, this is the
background color on a splash page. Label is `Quaternary motif`
```
   color.

```
**•** `MotifZeronaryComplementColor—Font color used with`
```
   zeronaryColor. Label is Zeronary motif colors
   complement color.

```
**•** `MotifPrimaryComplementColor—Font color used with`
```
   primaryColor. Label is Primary motif colors complement
   color.

```

-----

Not used for the Salesforce mobile app branding.

**•** `MotifTertiaryComplementColor—Font color used with`
```
  tertiaryColor. Label is Tertiary motif colors
  complement color.

```
Not used for the Salesforce mobile app branding.

**•** `MotifQuaternaryComplementColor—Font color used with`
```
  quaternaryColor. Label is Quaternary motif colors
  complement color.

```
Not used for the Salesforce mobile app branding.

**•** `PageHeader—An image that appears on the header of the pages. Can`
be an .html, .gif, .jpg, or .png file. Label is `Page Header.`

Not used for the Salesforce mobile app branding.

**•** `PageFooter—An image that appears on the footer of the pages. Must`
be an .html file. Label is `Page Footer.`

Not used for the Salesforce mobile app branding.

**•** `LoginFooterText—The text that appears in the footer of the login`
page. Label is Footer text displayed on the login page.

Not used for the Salesforce mobile app branding.

**•** `LoginLogoImageId—The logo that appears on the login page for`
external users. In the Salesforce mobile app, this logo also appears on the
Experience Cloud site splash page. Label is `Logo image displayed`
```
  on the login page.

```
**•** `LargeLogoImageId—Only used for the Salesforce mobile app. The`
logo that appears on the splash page when you start the Salesforce mobile
app. Label is `Large logo image.`

**•** `SmallLogoImageId—Only used for the Salesforce mobile app. The`
logo that appears on the publisher in the Salesforce mobile app. Label is
```
  Small logo image.

```
**•** `StaticLogoImageURL—The logo that appears on the login page for`
external users. Label is `Static logo image url.`

**•** `LoginQuaternaryColor—The background color that appears on the`
Experience Cloud site login page for external users. Label is `Login`
```
  background color.

```
**•** `LoginRightFrameUrl—The URL to the contents that appears on right`
side of the Experience Cloud site login page for external users. Label is Login
```
  right frame url.

```
**•** `LogoAssetId—Navigation tile menu item images. Label is` `Logo`
```
  asset image.

```
**•** `LoginPrimaryColor—The background color of the login button. Label`
is `Login primary color.`


-----

```
AssetSourceId
CustomBrandId

```


**•** `LoginBackgroundImageUrl—The path to the image URL that`
appears as the background on the Experience Cloud site’s login page. Label
is `Background image url.`

**•** `LargeLogoAssetId—Navigational topic images. Label is` `Large`
```
   logo asset image.

```
**•** `MediumLogoAssetId—Featured topic images. Label is` `Medium`
```
   logo asset image.

```
**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

ID of the document uploaded to the Documents folder if the value of
`AssetCategory` is:

**•** `PageHeader`

**•** `PageFooter`

**•** `LoginLogoImageId`

**•** `LargeLogoImageId`

**•** `SmallLogoImageId`

ID of the content asset if the value of the `AssetCategory` is:

**•** `LogoAssetId`

**•** `LargeLogoAssetId`

**•** `MediumLogoAssetId`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the associated CustomBrand .

This is a relationship field.

**Relationship Name**
CustomBrand

**Relationship Type**
Lookup

**Refers To**
CustomBrand


-----

```
ForeignKeyAssetId
TextAsset

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

This field was removed in API version 41.0, and is available in earlier versions for
backward compatibility only. Use `AssetSourceId` instead.

ID of the document used if the value of `AssetCategory is` `PageHeader,`
```
  PageFooter, or LoginLogoImageId.

```
**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Text used if the `AssetCategory` is `LoginFooterText.`


Use this object to add basic branding elements—color scheme, header or footer images, login page logo, or footer text—to the branding
scheme ( CustomBrand ) for your Experience Cloud site. You must have Create and Manage Experiences to customize site branding.

If you’re using digital experiences in the Salesforce mobile app, the loading page shows the logo.

SEE ALSO:

Network
