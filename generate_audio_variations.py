import asyncio
import edge_tts
import os

script_text = """
Welcome to the Active Recall Pocket Guide for the Markup Languages and Web Technologies Exam.
This is a rapid audio cram session covering all 9 sections of the syllabus.
Listen carefully to the core rules, and pay special attention to the exam traps at the end of each section.

Section 1: HTML 5 Semantics.
Core Definitions:
Article: Used for self-contained, independent, reusable content like a blog post.
Section: Used for a thematic grouping of content, usually with a heading.
Aside: Used for content indirectly related to the main content, like a sidebar.
Main: Represents the key content of the body. It must be unique, meaning only one per page.
Figure and Figcaption: Used for self-contained flow content with a caption.

Display and Validation:
Block versus Inline: div and p are block level elements. span and a are inline level elements.
Inputs: Important attributes include required, placeholder, and pattern, which defines a regular expression to validate the input.

Exam Trap for HTML 5 Semantics:
Never nest a main element inside a header, footer, nav, or aside. Also, a section should always contain a heading, like an h1 through h6.

Section 2: CSS Specificity and Selectors.
Specificity Vector Formula:
Remember the order: Inline, ID, Class, Element.
Inline Styles have a specificity of 1, 0, 0, 0.
ID Selectors have a specificity of 0, 1, 0, 0.
Class, Attribute, and Pseudo-classes have a specificity of 0, 0, 1, 0.
Element and Pseudo-elements have a specificity of 0, 0, 0, 1.
The Universal Selector and Combinators have a specificity of 0, 0, 0, 0.

Special Rules:
The not, is, and has pseudo-classes have no specificity themselves; their arguments dictate the specificity.
The important flag overrides everything regardless of the specificity vector.

Exam Trap for CSS Specificity:
If two selectors have equal specificity, the one declared last in the stylesheet wins. Also, class selectors always beat element selectors. For example, a single class always beats any number of nested element selectors.

Section 3: XML Basics and Namespaces.
Syntax Guidelines:
Case Sensitivity: Tags and attributes are strictly case-sensitive.
Root element: An XML document must have exactly one root element.
All tags must close.
Attributes must be enclosed in quotes.
Characters to escape include the less than sign, escaped as ampersand l t semicolon, and the ampersand, escaped as ampersand a m p semicolon.

Namespaces:
Their purpose is to avoid tag naming conflicts by using unique URIs.
The syntax is x m l n s colon prefix equals U R I. 

Exam Trap for XML Basics:
The XML declaration must be on the very first line, with no preceding spaces or blank lines. Furthermore, Namespace URIs do not need to be resolvable or exist online; they are simply unique identifier strings.

Section 4: XML Schema, or X S D.
Type Classification:
Simple Type: Can contain only text. No child elements, and no attributes.
Complex Type: Can contain child elements and attributes.

Compositors and Occurrences:
Sequence: Children must appear in the exact order declared.
All: Children can appear in any order, but the maximum occurrence is 1.
Choice: Allows only one of the child elements to appear.
For occurrences, the default minOccurs and maxOccurs is 1. For infinite occurrences, use the keyword unbounded.

Exam Trap for XML Schema:
Attributes inside a complex type must always be declared after the compositor, and they are always simple types. Also, remember to set elementFormDefault equals qualified so elements are properly bound to the target namespace.

Section 5: X Path and X Query.
X Path Shortcuts and Axes:
A single slash represents the root node or direct child.
A double slash represents descendant or self, meaning it searches anywhere.
The at symbol selects attributes.
A single dot selects the current node, while a double dot selects the parent node.
An asterisk is a wildcard that matches any element.
Common functions include count, sum, contains, and normalize-space.

X Query FLWOR Expression Mnemonic:
Remember the acronym FLWOR: For, Let, Where, Order by, Return.

Exam Trap for X Path:
X Path node indices are 1-indexed, not 0-indexed. For example, item bracket 1 bracket selects the first item, not the second.

Section 6: X S L T Transformations.
Basic Core Elements:
The root is xsl:stylesheet or xsl:transform.
To define a template rule, use xsl:template match.
To process child rules, use xsl:apply-templates.
To output a text value, use xsl:value-of.
To loop over nodes, use xsl:for-each.

Special Features:
For conditionals, use xsl:if, or the combination of xsl:choose and xsl:when.
Attribute Value Templates allow you to use curly braces inside attribute values to evaluate expressions.

Exam Trap for X S L T:
If no template matches a node, X S L T has a built-in default rule that recursively processes children and writes out their text nodes to the output. Always match nodes correctly to prevent unwanted text bleeding into your output.

Section 7: JSON and Schema.
JSON Data Types and Syntax:
Allowed types are String, Number, Object, Array, Boolean, and Null. There is no Date or Undefined type.
Keys must always be double-quoted strings. Single quotes will cause a syntax error.
Trailing commas are strictly forbidden in arrays and objects.

JSON Schema Keywords:
Structure is defined by type, properties, and additionalProperties.
Mandatory fields are defined by the required keyword, which takes an array of strings.
Validation uses minimum and maximum for numbers, and pattern for string regular expressions.

Exam Trap for JSON:
Comments are not allowed in standard JSON. In JSON Schema, the required keyword is an array declared at the object level, not a property attribute like it is in XSD.

Section 8: H T T P and REST APIs.
Methods and Verbs:
GET is used to retrieve data. It is safe and idempotent.
POST is used to create a resource. It is neither safe nor idempotent.
PUT is used to replace a resource. It is idempotent but not safe.
PATCH is for partial updates. It is normally neither safe nor idempotent.
DELETE is used to remove a resource. It is idempotent but not safe.

HTTP Status Codes:
100 level codes are Informational. 200 level codes represent Success, like 201 Created. 300 level codes are Redirects. 400 level codes are Client Errors, like 401 Unauthorized or 403 Forbidden. 500 level codes are Server Errors.

Exam Trap for H T T P:
Safe methods cannot change server state. Idempotency means multiple identical requests have the exact same effect as a single request. Remember that 401 means unauthenticated, while 403 means authenticated but unauthorized due to insufficient permissions.

Section 9: C S V Standard, R F C 4180.
Rules:
The standard delimiter is a comma, though local formats often use a semicolon.
If fields contain commas, newlines, or quotes, they must be enclosed in double quotes.
A double quote inside a quoted field is escaped by preceding it with another double quote.
The standard line break must use C R L F.

Exam Trap for C S V:
C S V has no official metadata mechanism to define column types. Empty lines at the end of the file can cause parser issues. Also, C S V does not natively support nested or hierarchical structures unlike XML and JSON.

This concludes the Active Recall Pocket Guide. Good luck on your exam!
"""

variations = {
    "us_male": ("en-US-SteffanNeural", "markup_audio_guide_us_male.mp3"),
    "us_female": ("en-US-JennyNeural", "markup_audio_guide_us_female.mp3"),
    "uk_male": ("en-GB-RyanNeural", "markup_audio_guide_uk_male.mp3"),
    "uk_female": ("en-GB-SoniaNeural", "markup_audio_guide_uk_female.mp3")
}

async def generate():
    os.makedirs("D:/CZUU/MARKUP_EXAM_SUITE", exist_ok=True)
    for key, (voice, filename) in variations.items():
        filepath = os.path.join("D:/CZUU/MARKUP_EXAM_SUITE", filename)
        print(f"Generating {key} version with voice {voice}...")
        communicate = edge_tts.Communicate(script_text, voice, rate="+5%")
        await communicate.save(filepath)
        print(f"Saved: {filepath}")

if __name__ == "__main__":
    asyncio.run(generate())
