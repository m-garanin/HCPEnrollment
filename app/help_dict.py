#-*- coding:utf-8 -*-
HELP_DICT = {}

def add(key, txt):
    HELP_DICT[key] = txt


##############################################################################################
##  Enrollment action requested (check all that apply)
##############################################################################################
add("001", """
check if the applicant is not currently enrolled in the Medi-Cal program as a provider with an active provider number.
Include the NPI (or Denti-Cal provider number if applicable) for the business address indicated in item 4.
""") # TODO: item 4 ???

add("002","""
check if the applicant is currently enrolled in the Medi-Cal program and is requesting to relocate to a 
new business address and vacate the old location. Indicate the business address applicant is moving from.
""")

add("003", """
check if the applicant is currently enrolled in the Medi-Cal program and is requesting enrollment for an
additional business location.
""")

add("004","""
check if a new Taxpayer Identification Number (TIN) was issued by the IRS.
""")

add("005", """
check if there is a change of ownership as defined in CCR, Title 22, Section 51000.6. Indicate the effective
date in the space provided.
""")

add("006", """
check if there is a cumulative change of 50
percent or more in the person(s) with an ownership or control interest, as defined in CCR, Title 22, Section 51000.15, since the
information provided in the last complete application package that was approved for enrollment. Indicate the effective date in the space
provided.
""")


add("007", """
check if 50 percent or more of the assets owned by the corporation, at the location for which
a provider number has been issued, are sold or transferred. Indicate the effective date in the space provided.
""")

add("008", """
check if the applicant is currently enrolled as a Medi-Cal provider and has been requested by the Department
to apply for continued enrollment in the Medi-Cal program. Do not check this box unless you have received notification from the
Department, pursuant to CCR, Title 22, Section 51000.55. List active provider number(s) in the space provided.
""")

add("009", """
Check the box labeled “I intend to use my current . . . .” if you intend to use your current provider number to bill for services delivered
at this location while this application request is pending. This action places the provider on provisional provider status, pursuant to
CCR, Title 22, Section 51000.51.
""")


##############################################################################################
##  Medi-Cal Application Fee (check all that apply)
##############################################################################################    
add("011", """
Check the box labeled “I am requesting enrollment as an individual …” if you are requesting enrollment as an individual nonphysician
practitioner. These providers are exempt from paying the application fee pursuant to W&I Code Section 14043.25(d) and the provider
bulletin, “Medi-Cal Application Fee Requirements for Compliance with 42 Code of Federal Regulations Section 455.460,” January 2013.
""")

add("012", """
Check the box labeled “I am currently enrolled in the Medicare program…” if you are currently enrolled in the Medicare program at the
business address indicated on page 4, item 4 of the application, and under the legal name listed on page 4, item 1 of the application.
Provider locations are exempt from paying the fee if currently enrolled in Medicare pursuant to Welfare and Institutions (W&I) Code
Section 14043.25(d) and the provider bulletin, “Medi-Cal Application Fee Requirements for Compliance with 42 Code of Federal
Regulations Section 455.460,” January 2013. Verification is required: provide an official notice from the enrolling agency that specifies
the applicant’s/provider’s legal name and physical business address as identified on this application.
""") # TODO: page 4, item 1

add("013", """
Check the box labeled “I am currently enrolled in another State’s…” if you are currently enrolled in another State’s Medicaid or
Children’s Health Insurance Program (CHIP) at the business address indicated on page 4, item 4 of the application, and under the legal
name listed on page 4, item 1 of the application. Provider locations are exempt from paying the fee if currently enrolled in another
State’s Medicaid or CHIP pursuant to W&I Code Section 14043.25(d) and the provider bulletin, “Medi-Cal Application Fee Requirements
for Compliance with 42 Code of Federal Regulations Section 455.460,” January 2013. Verification is required: provide an official notice
from the enrolling agency that specifies the applicant’s/provider’s legal name and physical business address as identified on this
application.
""") # TODO: page 4, item 4

add("014", """
Check the box labeled “I have paid the application fee…” if you have paid the application fee to a Medicare contractor or another State’s
Medicaid or CHIP for the enrollment of the business address indicated on page 4, item 4 of the application, and under the legal name
listed on page 4, item 1 of the application. Providers are exempt from paying the fee if they have already paid the fee to a Medicare
contractor or another State’s Medicaid or CHIP for the same business address pursuant to W&I Code Section 14043.25(d) and the
provider bulletin, “Medi-Cal Application Fee Requirements for Compliance with 42 Code of Federal Regulations Section 455.460,”
January 2013. Verification is required: provide official proof of payment that specifies the applicant’s/provider’s legal name and physical
business address as identified on this application.
""") # TODO: page 4, item 1

add("015", """
Check the box labeled “I have included an application fee…” if you included with the application either an application fee cashier’s
check, fee waiver request, or both. Providers that do not meet the exemptions specified in the above boxes are required to pay the fee
pursuant to W&I Code Section 14043.25(d) and the provider bulletin “Medi-Cal Application Fee Requirements for Compliance with 42
Code of Federal Regulations Section 455.460,” January 2013. DHCS can only accept a cashier’s check as payment of the
application fee – made payable to the State of California, Department of Health Care Services.
""")

##############################################################################################
## Type of entity (check one) 
##############################################################################################   
add("020", """
check the box which applies to your business structure. Your corporate status will be verified using the corporate
number and state in which incorporated. If a partnership, you must attach a legible copy of the partnership agreement. If you check
"other," list the type of legal entity.
""") # NOTES: not used in model


##############################################################################################
## HELP BY FIELD NUMBERS
##############################################################################################

##############################################################################################
## 1-10
##############################################################################################
add("1", """ 
“Legal name” is the name listed with the Internal Revenue Service (IRS).
""")

add("2", """
“Business name” is the name of the applicant or provider if different from that listed in number 1. If this is a fictitious business name,
provide the Fictitious Business Name Statement/Permit number and effective date. Attach a legible copy of the recorded/stamped
Fictitious Business Name Statement/Permit to the application.
""")

add("3", """
“Business telephone number” is the primary business telephone number used at the business address. A beeper number, cell
phone, answering service, pager, facsimile machine, biller or billing service, or answering machine shall not be used as the primary
business telephone.
""")

add("4", """
"Business address" is the actual business location including the street name and number, room or suite number or letter, city,
county, state, and nine-digit ZIP code. A post office or commercial box is not acceptable.
a. Check whether the business address is a licensed health facility as defined in Sections 1250,1250.2 and 1250.3 of the Health
and Safety Code. Check whether services will be rendered at only the business address indicated. If not, you must submit
a separate application for each business address unless you qualify for an exception pursuant to Welfare and Institutions
Code Section 14043.15(b)(2). See the "Facility-Based Provider" bulletin on the "Provider Enrollment" page of the Medi-Cal
Web site (www.medi-cal.ca.gov) for the requirements to qualify for that exception.
""") # used in formfields

add("5", """
"Pay-to address" is the address at which the applicant or provider wishes to receive payment. The pay-to address should include,
as applicable, the post office box number, street number and name, room or suite number or letter, city, state, and nine-digit ZIP
code.
""") # used in formfields

add("6", """
"Mailing address" is the location at which the applicant or provider wishes to receive general Medi-Cal correspondence. General
Medi-Cal correspondence includes bulletin updates and Provider Manual updates.
""") # used in formfields

add("7", """
"Previous business address" is the address where the applicant or provider was previously enrolled. If the applicant or provider is
not submitting an application for a change of location, enter N/A.
""") # used in formfields

add("8", """
Enter the license/certificate number, or other approval to provide health care, of the applicant or provider. Attach a legible copy of
the license, certificate, or approval. Enter the effective date and the expiration date of the license/certificate number, or other
approval.
""") 

add("9", """
Enter the provider type. See list in CCR, Title 22, Section 51051.
""") 

add("10", """
Enter any additional NPI for the business address indicated in item 4, registered with other carriers including, but not limited to
Medicare. Attach CMS/NPPES confirmation for each. Providers not eligible to receive an NPI (atypical providers) should submit
a Medicare billing number.
""") # TODO: item 4



##############################################################################################
## 11-20
##############################################################################################
add("11", """
Enter each taxonomy code(s) associated with your NPI. Attach additional sheet(s) if needed.
""") # TODO: attach ?

add("12", """
Enter the Taxpayer Identification Number (TIN) issued by the IRS under the name of the applicant or provider. Attach a legible
copy of the IRS Form 941, Form 8109-C, Letter 147-C, or Form SS-4 (Confirmation Notification).
""")

add("13", """
If the business is a sole proprietorship not using a TIN, provide the social security number of the sole proprietor. (See Privacy
Statement on page 5)
""") # TODO: page 5

add("14", """
Nurse Practitioners only—enter the duration of the nurse practitioner training program and the school at which the nurse
practitioner training program was completed.
""")

add("15", """
Nurse Practitioners only—enter clinical and didactic training or equivalent experience completed. Attach a legible copy.
""")

add("16", """
Enter the Clinical Laboratory Improvement Amendment (CLIA) certificate number. Attach a legible copy of the CLIA certificate.
If this does not apply to you, enter “N/A”.
""")

add("17", """
Enter the State Laboratory License/Registration number. Attach a legible copy of the license/registration. If this does not apply
to you, enter N/A.
""")

add("18", """
Enter the driver’s license or state-issued identification number and state of issuance of any individual named in number 1.
Attach a legible copy to the application. The driver’s license or state-issued identification number shall be issued within the 50
United States or the District of Columbia.
""")

add("19", """
Enter the name of the insurance company, insurance policy number, date policy issued, expiration
date of policy, insurance agent's name and insurance agent's telephone number. You must attach a copy of your certificate of
insurance for the identified business address to the application.
""") # used in forms

add("20", """
Enter the name of the insurance company, insurance policy number, date policy
issued, expiration date of policy, insurance agent's name and insurance agent's telephone number. You must attach a copy of
your certificate of insurance to the application.
""") # used in forms


##############################################################################################
## 21-33
##############################################################################################
add("21", """
Check the appropriate box to indicate whether you have Workers’ Compensation insurance as required by state law. If
applicable, attach proof. If not applicable, check N/A and provide an explanation.
""")

add("22", """
Enter the date of birth of the individual named in number 1, if applicable. If not applicable, enter N/A.
""") # TODO: number 1

add("23", """
Check the gender of the individual named in number 1, if applicable. If not applicable, enter N/A.
""") # TODO: number 1

add("24", """
Enter any local business license or permit numbers for any city and/or county where you conduct your business and attach
copies to the application. If this does not apply to you, enter N/A and provide an explanation.
""")

add("25", """
Enter the Seller’s Permit number issued by the State Board of Equalization. Attach a legible copy of the Seller’s Permit. If this
does not apply to you, enter N/A.
""")

add("26", """
“Printed name of provider”—print the last, first, and middle name of the person who is signing the application. The application
must be signed by a person who is authorized to legally bind the provider or applicant.
""")

add("27", """
Check the gender of the individual named in number 26.
""") # TODO: number 26

add("28", """
Enter the driver’s license or state-issued identification number and state of issuance of the individual named in number 26.
Attach a legible copy to the application.
""") # TODO: number 26

add("29", """
Enter the date of birth of the individual named in number 26.
""") # TODO: number 26

add("30", """
Enter the social security number of the individual named in number 26. Provision of the social security number is optional (See
Privacy Statement on page 5).
""") # TODO: page 5

add("31", """
An original signature of the individual named in number 26 is required. Also provide the title of the person signing the
application. Include the city, state, and the date where and when the application was signed. See CCR, Title 22,
Section 51000.30(a)(2)(B) to determine whether you have the authority to sign this application.
""") # used in forms TODO: number 26,

add("32", """
Applicants and providers licensed pursuant to Division 2 (commencing with Section 500) of the Business and Professions
Code, the Osteopathic Initiative Act, or the Chiropractic Initiative Act, ARE NOT REQUIRED to have this form notarized. If it 
must be notarized, the Certificate of Acknowledgement signed by the Notary Public must be in the form specified in
Section 1189 of the Civil Code.
""")

add("33", """
To assist in the timely processing of the application package, enter the name, e-mail address, and telephone number of the
individual who can be contacted by Provider Enrollment staff to answer questions regarding the application package. Failure
to include this information may result in the application package being returned deficient for item(s) that an applicant can readily
provide by fax or telephone.
""") # used in forms
