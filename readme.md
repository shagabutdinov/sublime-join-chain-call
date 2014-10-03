# Sublime JoinChainCall plugin

Handy plugin that automate joining/unjoining chain calls. Especially handy when
usign with jquery call-chains.


### Demo

![Demo](https://raw.github.com/shagabutdinov/sublime-join-chain-call/master/demo/demo.gif "Demo")


### Installation

This plugin is part of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
plugin set. You can install sublime-enhanced and this plugin will be installed
automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
package.


### Usage

1. Join chain call

  ```
  # before
  $('.class1'). # cursor should be outside of brackets
    find('.class2').
    find('.class3')

  # after
  $('.class1').find('.class2').find('.class3')
  ```

2. Unjoin chain call

  ```
  # before
  $('.class1').find('.class2').find('.class3') # cursor should be outside of brackets

  # after
  $('.class1').
    find('.class2').
    find('.class3')
  ```


### Commands

| Description               | Keyboard shortcut | Command palette        |
|---------------------------|-------------------|------------------------|
| Toggle chain call joining | ctrl+alt+v        | JoinChainCall: toggle  |
| Join chain call           | ctrl+m, j         | JoinChainCall: join    |
| Unjoin chain call         | ctrl+m, ctrl+j    | JoinChainCall: unjoin  |


### Dependencies

- https://github.com/shagabutdinov/sublime-statement
- https://github.com/shagabutdinov/sublime-expression