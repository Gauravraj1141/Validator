import json


class NewValidator:

    def validate_schema(self,json_file,schema_file)->bool:
        """
        Validate a JSON file against a given schema file.
        :param json_file: Path to the JSON file to be validated.
        :type json_file: str
        :param schema_file: Path to the schema file for validation.
        :type schema_file: str
        :return: True if validation succeeds, False otherwise.
        :rtype: bool
        """
        with open(schema_file) as s_file:
            schema_data = json.load(s_file)


        with open(json_file) as j_file:
            json_data = json.load(j_file)

        return(
            self.validate_required_fields(json_data,schema_data["required_fields"])
            and
            self.validate_fields_values(json_data,schema_data["field_value_set"])
        )

    def validate_required_fields(self,json_data,required_fields)->bool:
        """
        Validate that the required fields are present in the JSON data.
        :param json_data: The JSON data to be validated.
        :type json_data: dict
        :param required_fields: List of required field names.
        :type required_fields: List[str]
        :return: True if validation succeeds, False otherwise.
        :rtype: bool
        """
        for required_field in required_fields:
            if required_field not in json_data:
                print(f"'{required_field}' is required field")
                return False
        return True


    def validate_fields_values(self,json_data,schema_field_value_data)->bool:
        """
        Validate that fields have values within a predefined set.
        :param json_data: The JSON data to be validated.
        :type json_data: dict
        :param schema_field_value_data: Dictionary mapping field names to allowed values.
        :type schema_field_value_data: dict
        :return: True if validation succeeds, False otherwise.
        :rtype: bool
        """
        for field , allow_values in schema_field_value_data.items():
            if json_data[field] not in allow_values:
                print(f"Validation failed: '{field}' has an invalid value.")
                return False
        return True


validation = NewValidator()

result = validation.validate_schema(json_file="dummydata.json",schema_file="schema.json")

if result:
    print("overall validation successfull")
else:
    print("overall validation failed")