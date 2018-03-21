# thoughts
## TLDR
* looks really good. it's a good first step and i'm looking forward to seeing how this progresses. i don't really see any red flags. a lot of naming suggestions.
## Files and directories
* consider a root level 'html' directory, similar to how you have a directory for css and images
  * i think that having an html directory for everything but the root index.html file would make things a little more consistent
* consider sticking with lower case
  * if the naming convention is to always use lower case, it'll minimize case-based typos
  * some operating systems are case senstitive
    * eg. mine. some images are showing up as broken because the case of file names being referenced in the html don't consistently match the case of the actual file names
* consider grouping your images in such a way that they correspond to the files/directories where there used
  * again, i think it would make things more consistent
  * like having a 'countries' directory, and subdirectories for each country and they would contain images that are only referenced in the corresponding country html file
  * and having a 'common' or something directory for any shared assets
* consider isolating third-party CSS from your CSS
  * they currently share the same directory
  * since it's unlikely someone would be making direct changes to third-party code, it should be easy to distinguish it from yours
* alternatively, consider including third-party CSS from a CDN
  * https://www.bootstrapcdn.com/
  * it spares you from having to manage it in your repo
## CSS
* you can probably remove the reset css at the beginning
  * bootstrap already does this with normalize.css. See: http://getbootstrap.com/docs/3.3/css/#overview-normalize
* consider sticking to lower case for your class names
  * more tips on naming: https://medium.freecodecamp.org/css-naming-conventions-that-will-save-you-hours-of-debugging-35cea737d849
  * there are other naming conventions like BEM but probably not worth looking into until you start writing more complicated things
* also, consider sticking to singular names. eg. instead of `.CountryPages`, use `.country-page`
  * for me, plural implies a collection of something ie. an element with the class `.CountryPages` is one that contains several `.CountryPage` elements
* i'm seeing rules overriding styles for html tags and third-party rules
  * this can get harder to maintain as you add and change rules because an existing rule is too generic and conflicts with whatever additions/changes are being made. eg:
    * there's a rule for `.glyphicon` under a comment that says `/* header and footer */`. despite the comment, that rule is global and applies to any element with that class
    * there are rules directly on for h2, h3
  * consider a root class or parent classes (if it makes sense)
    * `.sk-header .glyphicon, .sk-footer .glyphicon {...}`
    * `.sk h3 {...}`
  * consider using dedicated, specific classes
    * `.sk-footer-glyphicon, .sk-header-glyphicon {...}`
* consider breaking up your main.css file
  * not necessarily right now but as it grows it might be harder to maintain or understand what each rule/section is for
  * there are many ways to go about this but one is based on the intent of the rules
    * eg. it's common to see something like typography.css or forms.css where you would establish global rules concerning themselves with how things like headers and paragraphs or input elements should look across your site and then you would additionally have more specific files, like country-pages.css where you can have a .country-page
## HTML
* looks fine but i'm not an expert on HTML semantics
## README.md
* make better use of markdown syntax to add style
  * see https://help.github.com/articles/basic-writing-and-formatting-syntax/
* you can probably just have the getting started start with "This isn't meant..." and to include instructions on how to view your site, including the part to clone
* i'm not sure if you need the git and the vs code instructions
  * since it's on github, i think it will be implicitly understood that using git is a prereq
  * i don't see anything about contributing to or using the repo that is specific to VS Code
    * i think it still makes sense to say it's built with it though
