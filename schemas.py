SCHEMA_FOR_DEVELOPDB = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "Data",
    "Host",
    "Port",
    "Database",
    "User",
    "Password",
    "Schema"
  ],
  "properties": {
    "Data": {
      "$id": "#/properties/Data",
      "type": "string",
      "title": "The Data Schema",
      "default": "",
      "examples": [
        "pLSjFbcXoE"
      ],
      "pattern": "^(.*)$"
    },
    "Host": {
      "$id": "#/properties/Host",
      "type": "string",
      "title": "The Host Schema",
      "default": "",
      "examples": [
        "FfRs"
      ],
      "pattern": "^(.*)$"
    },
    "Port": {
      "$id": "#/properties/Port",
      "type": "integer",
      "title": "The Port Schema",
      "default": 0,
      "examples": [
        58492
      ]
    },
    "Database": {
      "$id": "#/properties/Database",
      "type": "string",
      "title": "The Database Schema",
      "default": "",
      "examples": [
        "xPLDnJ"
      ],
      "pattern": "^(.*)$"
    },
    "User": {
      "$id": "#/properties/User",
      "type": "string",
      "title": "The User Schema",
      "default": "",
      "examples": [
        "ObCsN"
      ],
      "pattern": "^(.*)$"
    },
    "Password": {
      "$id": "#/properties/Password",
      "type": "string",
      "title": "The Password Schema",
      "default": "",
      "examples": [
        "VlgTeMaP"
      ],
      "pattern": "^(.*)$"
    },
    "Schema": {
      "$id": "#/properties/Schema",
      "type": "string",
      "title": "The Schema Schema",
      "default": "",
      "examples": [
        "EZQleQYh"
      ],
      "pattern": "^(.*)$"
    }
  }
}

SCHEMA_FOR_TESTDB = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "Data",
    "Host",
    "Port",
    "Virtualhost",
    "User",
    "Password"
  ],
  "properties": {
    "Data": {
      "$id": "#/properties/Data",
      "type": "string",
      "title": "The Data Schema",
      "default": "",
      "examples": [
        "XVlBzgbaiC"
      ],
      "pattern": "^(.*)$"
    },
    "Host": {
      "$id": "#/properties/Host",
      "type": "string",
      "title": "The Host Schema",
      "default": "",
      "examples": [
        "MRAj"
      ],
      "pattern": "^(.*)$"
    },
    "Port": {
      "$id": "#/properties/Port",
      "type": "integer",
      "title": "The Port Schema",
      "default": 0,
      "examples": [
        29645
      ]
    },
    "Virtualhost": {
      "$id": "#/properties/Virtualhost",
      "type": "string",
      "title": "The Virtualhost Schema",
      "default": "",
      "examples": [
        "whTHc"
      ],
      "pattern": "^(.*)$"
    },
    "User": {
      "$id": "#/properties/User",
      "type": "string",
      "title": "The User Schema",
      "default": "",
      "examples": [
        "tcuAx"
      ],
      "pattern": "^(.*)$"
    },
    "Password": {
      "$id": "#/properties/Password",
      "type": "string",
      "title": "The Password Schema",
      "default": "",
      "examples": [
        "hxKQFDaF"
      ],
      "pattern": "^(.*)$"
    }
  }
}

SCHEMA_ERROR = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "error"
  ],
  "properties": {
    "error": {
      "$id": "#/properties/error",
      "type": "string",
      "title": "The Error Schema",
      "default": "",
      "examples": [
        "record not found"
      ],
      "pattern": "^(.*)$"
    }
  }
}