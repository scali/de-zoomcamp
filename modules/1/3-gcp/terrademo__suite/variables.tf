variable "credentials" {
  description = "My creds"
  default     = "./keys/my-creds.json"
}

variable "project" {
  description = "Project"
  default     = "de-zoom-camp-412008"

}

variable "location" {
  description = "project location"
  default     = "US"

}

variable "bq_dataset_name" {
  description = "dataset name"
  default     = "demo_dataset"

}

variable "gcs_bucket_name" {
  description = "bucket name"
  default     = "de-zoom-camp-412008-demo-bucket"

}

variable "gcs_storage_class" {
  description = "Bucket storage class"
  default     = "STANDARD"

}