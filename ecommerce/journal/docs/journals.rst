=====================================
Journal Service Ecommerce Integration
=====================================

The Journal Product enables organizations to provide educational
resources that are better surfaced outside of the course experience. For
more information on this service and to see the source code go here:
https://github.com/edx/journals

This module contains the necessary integrations to make the journal
product purchasable.

New Product Class for Journals
==============================

A product class is a type of product, like “course seat” or “course
entitlement”. A new product class is created for journals by running
<MIGRATION>. This writes a new row to the <product class table>

Fulfillment
-----------

For each new product class you must define how that order is fulfilled.

-  <EXPLAIN HOW FULFILLMENT MODULE IS DEFINED>

-  <POINT TO FULFILMENT LINE>

Refunds
-------
