This application needs a service to be created and bound to the app. It can be any service. It's just to show that the app can access VCAP_SERVICES variable from within the code.

Example:
cf create-service elephantsql turtle <service_instance_name>
cf bind-service <app_name> <service_instance_name>

