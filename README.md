airwellhvac
===========

Airwell IR control reverse-engineering

This is to document my efforts to reverse-engineer codes to control Airwell HVAC air conditioning unit. 

The goal is to reverse-engineer the protocol the AC is using and to build a IR transmitter to transmit the signals. The arduino-based unit should also be capable of receiving IR signals to capture if the original remote is used to change state of the A/C unit.

Project status:

* IR codes reverse engineered for normal operation modes
* simple webserver/dispatcher implemented
* extensive amount of code to help in further reverse-engineering
    * ASCII colour-coded packets visualisation
    * encoding of pulses into binary notation
    * simple textual notation (not found that one that useful)
    * geneted pulses visualisation

TODO
* fully reverse-engineer the "I feel" functionality - initial packet documented, 