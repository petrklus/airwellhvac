airwellhvac
===========

Airwell IR control reverse-engineering

This is to document my efforts to reverse-engineer codes to control Airwell HVAC air conditioning unit. 

The goal is to reverse-engineer the protocol the AC is using and to build a IR transmitter to transmit the signals. The arduino-based unit should also be capable of receiving IR signals to capture if the original remote is used to change state of the A/C unit.

Project status:

* IR codes reverse engineered for normal operation modes
* extensive amount of code to help in further reverse-engineering
    * ASCII colour-coded packets visualisation
    * encoding of pulses into binary notation
    * simple textual notation (not found that one that useful)
    * geneted pulses visualisation
* simple webserver/dispatcher implemented
    * receives light levels to determine AC unit operational state - OFF, STANDBY, ON
    * translates commands into series of pulse lenghts
    * serial communication with arduino communication subunit
    * status reporting for further integration
    * multi-threaded processing, only enqueue and process "latest" version of command info


TODO
* fully reverse-engineer the "I feel" functionality - initial packet documented, but further work needed