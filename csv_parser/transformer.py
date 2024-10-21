class DataTransformer:
    def __init__(self, first_name_prefix: str, surname_prefix: str):
        self.email_prefix = (
            first_name_prefix[0].lower() +
            surname_prefix[:2].lower() +
            '_'
        )

    def transform(self, parsed_rows):
        transformed_data = []
        for row in parsed_rows:
            candidate_dict = self.create_candidate_dict(row)
            job_title = self.get_job_title(row)
            transformed_data.append(candidate_dict)
        return transformed_data, job_title

    def get_job_title(self,row):
        job_title = row.get('Position')
        return job_title
    
    def create_candidate_dict(self, row):
        # Concatenate First Name and Last Name
        first_name = row.get('First Name', '') or ''
        last_name = row.get('Last Name', '') or ''
        name = f"{first_name} {last_name}".strip()

        # Modify Email with the prefix
        email = row.get('Email', '') or ''
        modified_email = self.email_prefix + email
        # modified_email = '222222nkol_test@gmail.com'

        # Phone
        phone = row.get('Phone', '') or ''

        # Concatenate Address fields
        address_parts = [
            row.get('Address', '') or '',
            row.get('Address 2', '') or '',
            row.get('City', '') or '',
            row.get('State', '') or '',
            row.get('Country', '') or '',
            row.get('Zip', '') or ''
        ]
        # Filter out empty strings and join with ', '
        address = ', '.join(filter(None, address_parts))

        # Source
        source = row.get('Referred By', '') or ''

        
        # Disqualified
        status = row.get('Status', '') or ''
        disqualified = status.strip().lower() == 'rejected'

        # Create the candidate dictionary
        candidate_dict = {
            'name': name,
            'email': modified_email,
            'phone': phone,
            'address': address,
            'domain': source,
            'disqualified': disqualified
        }

        return candidate_dict
