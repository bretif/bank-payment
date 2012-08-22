# -*- encoding: utf-8 -*-

pain_001_001_04_xsd = '''\
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema">
    <xs:element name="Document" type="Document"/>
    <xs:complexType name="AccountIdentification4Choice">
        <xs:sequence>
            <xs:choice>
                <xs:element name="IBAN" type="IBAN2007Identifier"/>
                <xs:element name="Othr" type="GenericAccountIdentification1"/>
            </xs:choice>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="AccountSchemeName1Choice">
        <xs:sequence>
            <xs:choice>
                <xs:element name="Cd" type="ExternalAccountIdentification1Code"/>
                <xs:element name="Prtry" type="Max35Text"/>
            </xs:choice>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="ActiveOrHistoricCurrencyAndAmount_SimpleType">
        <xs:restriction base="xs:decimal">
            <xs:fractionDigits value="5"/>
            <xs:totalDigits value="18"/>
            <xs:minInclusive value="0"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="ActiveOrHistoricCurrencyAndAmount">
        <xs:simpleContent>
            <xs:extension base="ActiveOrHistoricCurrencyAndAmount_SimpleType">
                <xs:attribute name="Ccy" type="ActiveOrHistoricCurrencyCode" use="required"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
    <xs:simpleType name="ActiveOrHistoricCurrencyCode">
        <xs:restriction base="xs:string">
            <xs:pattern value="[A-Z]{3,3}"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="AddressType2Code">
        <xs:restriction base="xs:string">
            <xs:enumeration value="ADDR"/>
            <xs:enumeration value="PBOX"/>
            <xs:enumeration value="HOME"/>
            <xs:enumeration value="BIZZ"/>
            <xs:enumeration value="MLTO"/>
            <xs:enumeration value="DLVY"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="AmountType3Choice">
        <xs:sequence>
            <xs:choice>
                <xs:element name="InstdAmt" type="ActiveOrHistoricCurrencyAndAmount"/>
                <xs:element name="EqvtAmt" type="EquivalentAmount2"/>
            </xs:choice>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="AnyBICIdentifier">
        <xs:restriction base="xs:string">
            <xs:pattern value="[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="Authorisation1Choice">
        <xs:sequence>
            <xs:choice>
                <xs:element name="Cd" type="Authorisation1Code"/>
                <xs:element name="Prtry" type="Max128Text"/>
            </xs:choice>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="Authorisation1Code">
        <xs:restriction base="xs:string">
            <xs:enumeration value="AUTH"/>
            <xs:enumeration value="FDET"/>
            <xs:enumeration value="FSUM"/>
            <xs:enumeration value="ILEV"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="BICFIIdentifier">
        <xs:restriction base="xs:string">
            <xs:pattern value="[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="BaseOneRate">
        <xs:restriction base="xs:decimal">
            <xs:fractionDigits value="10"/>
            <xs:totalDigits value="11"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="BatchBookingIndicator">
        <xs:restriction base="xs:boolean"/>
    </xs:simpleType>
    <xs:complexType name="BranchAndFinancialInstitutionIdentification5">
        <xs:sequence>
            <xs:element name="FinInstnId" type="FinancialInstitutionIdentification8"/>
            <xs:element maxOccurs="1" minOccurs="0" name="BrnchId" type="BranchData2"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="BranchData2">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="Id" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Nm" type="Max140Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="PstlAdr" type="PostalAddress6"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="CashAccount24">
        <xs:sequence>
            <xs:element name="Id" type="AccountIdentification4Choice"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Tp" type="CashAccountType2Choice"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Ccy" type="ActiveOrHistoricCurrencyCode"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Nm" type="Max70Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="CashAccountType2Choice">
        <xs:sequence>
            <xs:choice>
                <xs:element name="Cd" type="ExternalCashAccountType1Code"/>
                <xs:element name="Prtry" type="Max35Text"/>
            </xs:choice>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="CategoryPurpose1Choice">
        <xs:sequence>
            <xs:choice>
                <xs:element name="Cd" type="ExternalCategoryPurpose1Code"/>
                <xs:element name="Prtry" type="Max35Text"/>
            </xs:choice>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="ChargeBearerType1Code">
        <xs:restriction base="xs:string">
            <xs:enumeration value="DEBT"/>
            <xs:enumeration value="CRED"/>
            <xs:enumeration value="SHAR"/>
            <xs:enumeration value="SLEV"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="Cheque7">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="ChqTp" type="ChequeType2Code"/>
            <xs:element maxOccurs="1" minOccurs="0" name="ChqNb" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="ChqFr" type="NameAndAddress10"/>
            <xs:element maxOccurs="1" minOccurs="0" name="DlvryMtd" type="ChequeDeliveryMethod1Choice"/>
            <xs:element maxOccurs="1" minOccurs="0" name="DlvrTo" type="NameAndAddress10"/>
            <xs:element maxOccurs="1" minOccurs="0" name="InstrPrty" type="Priority2Code"/>
            <xs:element maxOccurs="1" minOccurs="0" name="ChqMtrtyDt" type="ISODate"/>
            <xs:element maxOccurs="1" minOccurs="0" name="FrmsCd" type="Max35Text"/>
            <xs:element maxOccurs="2" minOccurs="0" name="MemoFld" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="RgnlClrZone" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="PrtLctn" type="Max35Text"/>
            <xs:element maxOccurs="5" minOccurs="0" name="Sgntr" type="Max70Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="ChequeDelivery1Code">
        <xs:restriction base="xs:string">
            <xs:enumeration value="MLDB"/>
            <xs:enumeration value="MLCD"/>
            <xs:enumeration value="MLFA"/>
            <xs:enumeration value="CRDB"/>
            <xs:enumeration value="CRCD"/>
            <xs:enumeration value="CRFA"/>
            <xs:enumeration value="PUDB"/>
            <xs:enumeration value="PUCD"/>
            <xs:enumeration value="PUFA"/>
            <xs:enumeration value="RGDB"/>
            <xs:enumeration value="RGCD"/>
            <xs:enumeration value="RGFA"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="ChequeDeliveryMethod1Choice">
        <xs:sequence>
            <xs:choice>
                <xs:element name="Cd" type="ChequeDelivery1Code"/>
                <xs:element name="Prtry" type="Max35Text"/>
            </xs:choice>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="ChequeType2Code">
        <xs:restriction base="xs:string">
            <xs:enumeration value="CCHQ"/>
            <xs:enumeration value="CCCH"/>
            <xs:enumeration value="BCHQ"/>
            <xs:enumeration value="DRFT"/>
            <xs:enumeration value="ELDR"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="ClearingSystemIdentification2Choice">
        <xs:sequence>
            <xs:choice>
                <xs:element name="Cd" type="ExternalClearingSystemIdentification1Code"/>
                <xs:element name="Prtry" type="Max35Text"/>
            </xs:choice>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="ClearingSystemMemberIdentification2">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="ClrSysId" type="ClearingSystemIdentification2Choice"/>
            <xs:element name="MmbId" type="Max35Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="ContactDetails2">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="NmPrfx" type="NamePrefix1Code"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Nm" type="Max140Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="PhneNb" type="PhoneNumber"/>
            <xs:element maxOccurs="1" minOccurs="0" name="MobNb" type="PhoneNumber"/>
            <xs:element maxOccurs="1" minOccurs="0" name="FaxNb" type="PhoneNumber"/>
            <xs:element maxOccurs="1" minOccurs="0" name="EmailAdr" type="Max2048Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Othr" type="Max35Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="CountryCode">
        <xs:restriction base="xs:string">
            <xs:pattern value="[A-Z]{2,2}"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="CreditDebitCode">
        <xs:restriction base="xs:string">
            <xs:enumeration value="CRDT"/>
            <xs:enumeration value="DBIT"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="CreditTransferTransaction1">
        <xs:sequence>
            <xs:element name="PmtId" type="PaymentIdentification1"/>
            <xs:element maxOccurs="1" minOccurs="0" name="PmtTpInf" type="PaymentTypeInformation19"/>
            <xs:element name="Amt" type="AmountType3Choice"/>
            <xs:element maxOccurs="1" minOccurs="0" name="XchgRateInf" type="ExchangeRate1"/>
            <xs:element maxOccurs="1" minOccurs="0" name="ChrgBr" type="ChargeBearerType1Code"/>
            <xs:element maxOccurs="1" minOccurs="0" name="ChqInstr" type="Cheque7"/>
            <xs:element maxOccurs="1" minOccurs="0" name="UltmtDbtr" type="PartyIdentification43"/>
            <xs:element maxOccurs="1" minOccurs="0" name="IntrmyAgt1" type="BranchAndFinancialInstitutionIdentification5"/>
            <xs:element maxOccurs="1" minOccurs="0" name="IntrmyAgt1Acct" type="CashAccount24"/>
            <xs:element maxOccurs="1" minOccurs="0" name="IntrmyAgt2" type="BranchAndFinancialInstitutionIdentification5"/>
            <xs:element maxOccurs="1" minOccurs="0" name="IntrmyAgt2Acct" type="CashAccount24"/>
            <xs:element maxOccurs="1" minOccurs="0" name="IntrmyAgt3" type="BranchAndFinancialInstitutionIdentification5"/>
            <xs:element maxOccurs="1" minOccurs="0" name="IntrmyAgt3Acct" type="CashAccount24"/>
            <xs:element maxOccurs="1" minOccurs="0" name="CdtrAgt" type="BranchAndFinancialInstitutionIdentification5"/>
            <xs:element maxOccurs="1" minOccurs="0" name="CdtrAgtAcct" type="CashAccount24"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Cdtr" type="PartyIdentification43"/>
            <xs:element maxOccurs="1" minOccurs="0" name="CdtrAcct" type="CashAccount24"/>
            <xs:element maxOccurs="1" minOccurs="0" name="UltmtCdtr" type="PartyIdentification43"/>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="InstrForCdtrAgt" type="InstructionForCreditorAgent1"/>
            <xs:element maxOccurs="1" minOccurs="0" name="InstrForDbtrAgt" type="Max140Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Purp" type="Purpose2Choice"/>
            <xs:element maxOccurs="10" minOccurs="0" name="RgltryRptg" type="RegulatoryReporting3"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Tax" type="TaxInformation3"/>
            <xs:element maxOccurs="10" minOccurs="0" name="RltdRmtInf" type="RemittanceLocation2"/>
            <xs:element maxOccurs="1" minOccurs="0" name="RmtInf" type="RemittanceInformation7"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="CreditorReferenceInformation2">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="Tp" type="CreditorReferenceType2"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Ref" type="Max35Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="CreditorReferenceType1Choice">
        <xs:sequence>
            <xs:choice>
                <xs:element name="Cd" type="DocumentType3Code"/>
                <xs:element name="Prtry" type="Max35Text"/>
            </xs:choice>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="CreditorReferenceType2">
        <xs:sequence>
            <xs:element name="CdOrPrtry" type="CreditorReferenceType1Choice"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Issr" type="Max35Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="CustomerCreditTransferInitiationV04">
        <xs:sequence>
            <xs:element name="GrpHdr" type="GroupHeader48"/>
            <xs:element maxOccurs="unbounded" minOccurs="1" name="PmtInf" type="PaymentInstruction6"/>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="SplmtryData" type="SupplementaryData1"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="DateAndPlaceOfBirth">
        <xs:sequence>
            <xs:element name="BirthDt" type="ISODate"/>
            <xs:element maxOccurs="1" minOccurs="0" name="PrvcOfBirth" type="Max35Text"/>
            <xs:element name="CityOfBirth" type="Max35Text"/>
            <xs:element name="CtryOfBirth" type="CountryCode"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="DatePeriodDetails">
        <xs:sequence>
            <xs:element name="FrDt" type="ISODate"/>
            <xs:element name="ToDt" type="ISODate"/>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="DecimalNumber">
        <xs:restriction base="xs:decimal">
            <xs:fractionDigits value="17"/>
            <xs:totalDigits value="18"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="DiscountAmountAndType1">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="Tp" type="DiscountAmountType1Choice"/>
            <xs:element name="Amt" type="ActiveOrHistoricCurrencyAndAmount"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="DiscountAmountType1Choice">
        <xs:sequence>
            <xs:choice>
                <xs:element name="Cd" type="ExternalDiscountAmountType1Code"/>
                <xs:element name="Prtry" type="Max35Text"/>
            </xs:choice>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="Document">
        <xs:sequence>
            <xs:element name="CstmrCdtTrfInitn" type="CustomerCreditTransferInitiationV04"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="DocumentAdjustment1">
        <xs:sequence>
            <xs:element name="Amt" type="ActiveOrHistoricCurrencyAndAmount"/>
            <xs:element maxOccurs="1" minOccurs="0" name="CdtDbtInd" type="CreditDebitCode"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Rsn" type="Max4Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="AddtlInf" type="Max140Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="DocumentType3Code">
        <xs:restriction base="xs:string">
            <xs:enumeration value="RADM"/>
            <xs:enumeration value="RPIN"/>
            <xs:enumeration value="FXDR"/>
            <xs:enumeration value="DISP"/>
            <xs:enumeration value="PUOR"/>
            <xs:enumeration value="SCOR"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="DocumentType5Code">
        <xs:restriction base="xs:string">
            <xs:enumeration value="MSIN"/>
            <xs:enumeration value="CNFA"/>
            <xs:enumeration value="DNFA"/>
            <xs:enumeration value="CINV"/>
            <xs:enumeration value="CREN"/>
            <xs:enumeration value="DEBN"/>
            <xs:enumeration value="HIRI"/>
            <xs:enumeration value="SBIN"/>
            <xs:enumeration value="CMCN"/>
            <xs:enumeration value="SOAC"/>
            <xs:enumeration value="DISP"/>
            <xs:enumeration value="BOLD"/>
            <xs:enumeration value="VCHR"/>
            <xs:enumeration value="AROI"/>
            <xs:enumeration value="TSUT"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="EquivalentAmount2">
        <xs:sequence>
            <xs:element name="Amt" type="ActiveOrHistoricCurrencyAndAmount"/>
            <xs:element name="CcyOfTrf" type="ActiveOrHistoricCurrencyCode"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="ExchangeRate1">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="UnitCcy" type="ActiveOrHistoricCurrencyCode"/>
            <xs:element maxOccurs="1" minOccurs="0" name="XchgRate" type="BaseOneRate"/>
            <xs:element maxOccurs="1" minOccurs="0" name="RateTp" type="ExchangeRateType1Code"/>
            <xs:element maxOccurs="1" minOccurs="0" name="CtrctId" type="Max35Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="ExchangeRateType1Code">
        <xs:restriction base="xs:string">
            <xs:enumeration value="SPOT"/>
            <xs:enumeration value="SALE"/>
            <xs:enumeration value="AGRD"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="ExternalAccountIdentification1Code">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="ExternalCashAccountType1Code">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="ExternalCategoryPurpose1Code">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="ExternalClearingSystemIdentification1Code">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="5"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="ExternalDiscountAmountType1Code">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="ExternalFinancialInstitutionIdentification1Code">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="ExternalLocalInstrument1Code">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="35"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="ExternalOrganisationIdentification1Code">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="ExternalPersonIdentification1Code">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="ExternalPurpose1Code">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="ExternalServiceLevel1Code">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="ExternalTaxAmountType1Code">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="FinancialIdentificationSchemeName1Choice">
        <xs:sequence>
            <xs:choice>
                <xs:element name="Cd" type="ExternalFinancialInstitutionIdentification1Code"/>
                <xs:element name="Prtry" type="Max35Text"/>
            </xs:choice>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="FinancialInstitutionIdentification8">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="BICFI" type="BICFIIdentifier"/>
            <xs:element maxOccurs="1" minOccurs="0" name="ClrSysMmbId" type="ClearingSystemMemberIdentification2"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Nm" type="Max140Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="PstlAdr" type="PostalAddress6"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Othr" type="GenericFinancialIdentification1"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="GenericAccountIdentification1">
        <xs:sequence>
            <xs:element name="Id" type="Max34Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="SchmeNm" type="AccountSchemeName1Choice"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Issr" type="Max35Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="GenericFinancialIdentification1">
        <xs:sequence>
            <xs:element name="Id" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="SchmeNm" type="FinancialIdentificationSchemeName1Choice"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Issr" type="Max35Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="GenericOrganisationIdentification1">
        <xs:sequence>
            <xs:element name="Id" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="SchmeNm" type="OrganisationIdentificationSchemeName1Choice"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Issr" type="Max35Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="GenericPersonIdentification1">
        <xs:sequence>
            <xs:element name="Id" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="SchmeNm" type="PersonIdentificationSchemeName1Choice"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Issr" type="Max35Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="GroupHeader48">
        <xs:sequence>
            <xs:element name="MsgId" type="Max35Text"/>
            <xs:element name="CreDtTm" type="ISODateTime"/>
            <xs:element maxOccurs="2" minOccurs="0" name="Authstn" type="Authorisation1Choice"/>
            <xs:element name="NbOfTxs" type="Max15NumericText"/>
            <xs:element maxOccurs="1" minOccurs="0" name="CtrlSum" type="DecimalNumber"/>
            <xs:element name="InitgPty" type="PartyIdentification43"/>
            <xs:element maxOccurs="1" minOccurs="0" name="FwdgAgt" type="BranchAndFinancialInstitutionIdentification5"/>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="IBAN2007Identifier">
        <xs:restriction base="xs:string">
            <xs:pattern value="[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="ISODate">
        <xs:restriction base="xs:date"/>
    </xs:simpleType>
    <xs:simpleType name="ISODateTime">
        <xs:restriction base="xs:dateTime"/>
    </xs:simpleType>
    <xs:simpleType name="Instruction3Code">
        <xs:restriction base="xs:string">
            <xs:enumeration value="CHQB"/>
            <xs:enumeration value="HOLD"/>
            <xs:enumeration value="PHOB"/>
            <xs:enumeration value="TELB"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="InstructionForCreditorAgent1">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="Cd" type="Instruction3Code"/>
            <xs:element maxOccurs="1" minOccurs="0" name="InstrInf" type="Max140Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="LocalInstrument2Choice">
        <xs:sequence>
            <xs:choice>
                <xs:element name="Cd" type="ExternalLocalInstrument1Code"/>
                <xs:element name="Prtry" type="Max35Text"/>
            </xs:choice>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="Max10Text">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="10"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="Max128Text">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="128"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="Max140Text">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="140"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="Max15NumericText">
        <xs:restriction base="xs:string">
            <xs:pattern value="[0-9]{1,15}"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="Max16Text">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="16"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="Max2048Text">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="2048"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="Max34Text">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="34"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="Max350Text">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="350"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="Max35Text">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="35"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="Max4Text">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="Max70Text">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="70"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="NameAndAddress10">
        <xs:sequence>
            <xs:element name="Nm" type="Max140Text"/>
            <xs:element name="Adr" type="PostalAddress6"/>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="NamePrefix1Code">
        <xs:restriction base="xs:string">
            <xs:enumeration value="DOCT"/>
            <xs:enumeration value="MIST"/>
            <xs:enumeration value="MISS"/>
            <xs:enumeration value="MADM"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="Number">
        <xs:restriction base="xs:decimal">
            <xs:fractionDigits value="0"/>
            <xs:totalDigits value="18"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="OrganisationIdentification8">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="AnyBIC" type="AnyBICIdentifier"/>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="Othr" type="GenericOrganisationIdentification1"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="OrganisationIdentificationSchemeName1Choice">
        <xs:sequence>
            <xs:choice>
                <xs:element name="Cd" type="ExternalOrganisationIdentification1Code"/>
                <xs:element name="Prtry" type="Max35Text"/>
            </xs:choice>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="Party11Choice">
        <xs:sequence>
            <xs:choice>
                <xs:element name="OrgId" type="OrganisationIdentification8"/>
                <xs:element name="PrvtId" type="PersonIdentification5"/>
            </xs:choice>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="PartyIdentification43">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="Nm" type="Max140Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="PstlAdr" type="PostalAddress6"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Id" type="Party11Choice"/>
            <xs:element maxOccurs="1" minOccurs="0" name="CtryOfRes" type="CountryCode"/>
            <xs:element maxOccurs="1" minOccurs="0" name="CtctDtls" type="ContactDetails2"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="PaymentIdentification1">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="InstrId" type="Max35Text"/>
            <xs:element name="EndToEndId" type="Max35Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="PaymentInstruction6">
        <xs:sequence>
            <xs:element name="PmtInfId" type="Max35Text"/>
            <xs:element name="PmtMtd" type="PaymentMethod3Code"/>
            <xs:element maxOccurs="1" minOccurs="0" name="BtchBookg" type="BatchBookingIndicator"/>
            <xs:element maxOccurs="1" minOccurs="0" name="NbOfTxs" type="Max15NumericText"/>
            <xs:element maxOccurs="1" minOccurs="0" name="CtrlSum" type="DecimalNumber"/>
            <xs:element maxOccurs="1" minOccurs="0" name="PmtTpInf" type="PaymentTypeInformation19"/>
            <xs:element name="ReqdExctnDt" type="ISODate"/>
            <xs:element maxOccurs="1" minOccurs="0" name="PoolgAdjstmntDt" type="ISODate"/>
            <xs:element name="Dbtr" type="PartyIdentification43"/>
            <xs:element name="DbtrAcct" type="CashAccount24"/>
            <xs:element name="DbtrAgt" type="BranchAndFinancialInstitutionIdentification5"/>
            <xs:element maxOccurs="1" minOccurs="0" name="DbtrAgtAcct" type="CashAccount24"/>
            <xs:element maxOccurs="1" minOccurs="0" name="InstrForDbtrAgt" type="Max140Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="UltmtDbtr" type="PartyIdentification43"/>
            <xs:element maxOccurs="1" minOccurs="0" name="ChrgBr" type="ChargeBearerType1Code"/>
            <xs:element maxOccurs="1" minOccurs="0" name="ChrgsAcct" type="CashAccount24"/>
            <xs:element maxOccurs="1" minOccurs="0" name="ChrgsAcctAgt" type="BranchAndFinancialInstitutionIdentification5"/>
            <xs:element maxOccurs="unbounded" minOccurs="1" name="CdtTrfTxInf" type="CreditTransferTransaction1"/>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="PaymentMethod3Code">
        <xs:restriction base="xs:string">
            <xs:enumeration value="CHK"/>
            <xs:enumeration value="TRF"/>
            <xs:enumeration value="TRA"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="PaymentTypeInformation19">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="InstrPrty" type="Priority2Code"/>
            <xs:element maxOccurs="1" minOccurs="0" name="SvcLvl" type="ServiceLevel8Choice"/>
            <xs:element maxOccurs="1" minOccurs="0" name="LclInstrm" type="LocalInstrument2Choice"/>
            <xs:element maxOccurs="1" minOccurs="0" name="CtgyPurp" type="CategoryPurpose1Choice"/>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="PercentageRate">
        <xs:restriction base="xs:decimal">
            <xs:fractionDigits value="10"/>
            <xs:totalDigits value="11"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="PersonIdentification5">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="DtAndPlcOfBirth" type="DateAndPlaceOfBirth"/>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="Othr" type="GenericPersonIdentification1"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="PersonIdentificationSchemeName1Choice">
        <xs:sequence>
            <xs:choice>
                <xs:element name="Cd" type="ExternalPersonIdentification1Code"/>
                <xs:element name="Prtry" type="Max35Text"/>
            </xs:choice>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="PhoneNumber">
        <xs:restriction base="xs:string">
            <xs:pattern value="\+[0-9]{1,3}-[0-9()+\-]{1,30}"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="PostalAddress6">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="AdrTp" type="AddressType2Code"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Dept" type="Max70Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="SubDept" type="Max70Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="StrtNm" type="Max70Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="BldgNb" type="Max16Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="PstCd" type="Max16Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="TwnNm" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="CtrySubDvsn" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Ctry" type="CountryCode"/>
            <xs:element maxOccurs="7" minOccurs="0" name="AdrLine" type="Max70Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="Priority2Code">
        <xs:restriction base="xs:string">
            <xs:enumeration value="HIGH"/>
            <xs:enumeration value="NORM"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="Purpose2Choice">
        <xs:sequence>
            <xs:choice>
                <xs:element name="Cd" type="ExternalPurpose1Code"/>
                <xs:element name="Prtry" type="Max35Text"/>
            </xs:choice>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="ReferredDocumentInformation3">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="Tp" type="ReferredDocumentType2"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Nb" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="RltdDt" type="ISODate"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="ReferredDocumentType1Choice">
        <xs:sequence>
            <xs:choice>
                <xs:element name="Cd" type="DocumentType5Code"/>
                <xs:element name="Prtry" type="Max35Text"/>
            </xs:choice>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="ReferredDocumentType2">
        <xs:sequence>
            <xs:element name="CdOrPrtry" type="ReferredDocumentType1Choice"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Issr" type="Max35Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="RegulatoryAuthority2">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="Nm" type="Max140Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Ctry" type="CountryCode"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="RegulatoryReporting3">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="DbtCdtRptgInd" type="RegulatoryReportingType1Code"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Authrty" type="RegulatoryAuthority2"/>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="Dtls" type="StructuredRegulatoryReporting3"/>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="RegulatoryReportingType1Code">
        <xs:restriction base="xs:string">
            <xs:enumeration value="CRED"/>
            <xs:enumeration value="DEBT"/>
            <xs:enumeration value="BOTH"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="RemittanceAmount2">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="DuePyblAmt" type="ActiveOrHistoricCurrencyAndAmount"/>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="DscntApldAmt" type="DiscountAmountAndType1"/>
            <xs:element maxOccurs="1" minOccurs="0" name="CdtNoteAmt" type="ActiveOrHistoricCurrencyAndAmount"/>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="TaxAmt" type="TaxAmountAndType1"/>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="AdjstmntAmtAndRsn" type="DocumentAdjustment1"/>
            <xs:element maxOccurs="1" minOccurs="0" name="RmtdAmt" type="ActiveOrHistoricCurrencyAndAmount"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="RemittanceInformation7">
        <xs:sequence>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="Ustrd" type="Max140Text"/>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="Strd" type="StructuredRemittanceInformation9"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="RemittanceLocation2">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="RmtId" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="RmtLctnMtd" type="RemittanceLocationMethod2Code"/>
            <xs:element maxOccurs="1" minOccurs="0" name="RmtLctnElctrncAdr" type="Max2048Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="RmtLctnPstlAdr" type="NameAndAddress10"/>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="RemittanceLocationMethod2Code">
        <xs:restriction base="xs:string">
            <xs:enumeration value="FAXI"/>
            <xs:enumeration value="EDIC"/>
            <xs:enumeration value="URID"/>
            <xs:enumeration value="EMAL"/>
            <xs:enumeration value="POST"/>
            <xs:enumeration value="SMSM"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="ServiceLevel8Choice">
        <xs:sequence>
            <xs:choice>
                <xs:element name="Cd" type="ExternalServiceLevel1Code"/>
                <xs:element name="Prtry" type="Max35Text"/>
            </xs:choice>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="StructuredRegulatoryReporting3">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="Tp" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Dt" type="ISODate"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Ctry" type="CountryCode"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Cd" type="Max10Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Amt" type="ActiveOrHistoricCurrencyAndAmount"/>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="Inf" type="Max35Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="StructuredRemittanceInformation9">
        <xs:sequence>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="RfrdDocInf" type="ReferredDocumentInformation3"/>
            <xs:element maxOccurs="1" minOccurs="0" name="RfrdDocAmt" type="RemittanceAmount2"/>
            <xs:element maxOccurs="1" minOccurs="0" name="CdtrRefInf" type="CreditorReferenceInformation2"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Invcr" type="PartyIdentification43"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Invcee" type="PartyIdentification43"/>
            <xs:element maxOccurs="3" minOccurs="0" name="AddtlRmtInf" type="Max140Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="SupplementaryData1">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="PlcAndNm" type="Max350Text"/>
            <xs:element name="Envlp" type="SupplementaryDataEnvelope1"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="SupplementaryDataEnvelope1">
        <xs:sequence>
            <xs:any namespace="##any" processContents="lax"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="TaxAmount1">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="Rate" type="PercentageRate"/>
            <xs:element maxOccurs="1" minOccurs="0" name="TaxblBaseAmt" type="ActiveOrHistoricCurrencyAndAmount"/>
            <xs:element maxOccurs="1" minOccurs="0" name="TtlAmt" type="ActiveOrHistoricCurrencyAndAmount"/>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="Dtls" type="TaxRecordDetails1"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="TaxAmountAndType1">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="Tp" type="TaxAmountType1Choice"/>
            <xs:element name="Amt" type="ActiveOrHistoricCurrencyAndAmount"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="TaxAmountType1Choice">
        <xs:sequence>
            <xs:choice>
                <xs:element name="Cd" type="ExternalTaxAmountType1Code"/>
                <xs:element name="Prtry" type="Max35Text"/>
            </xs:choice>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="TaxAuthorisation1">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="Titl" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Nm" type="Max140Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="TaxInformation3">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="Cdtr" type="TaxParty1"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Dbtr" type="TaxParty2"/>
            <xs:element maxOccurs="1" minOccurs="0" name="AdmstnZn" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="RefNb" type="Max140Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Mtd" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="TtlTaxblBaseAmt" type="ActiveOrHistoricCurrencyAndAmount"/>
            <xs:element maxOccurs="1" minOccurs="0" name="TtlTaxAmt" type="ActiveOrHistoricCurrencyAndAmount"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Dt" type="ISODate"/>
            <xs:element maxOccurs="1" minOccurs="0" name="SeqNb" type="Number"/>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="Rcrd" type="TaxRecord1"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="TaxParty1">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="TaxId" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="RegnId" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="TaxTp" type="Max35Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="TaxParty2">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="TaxId" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="RegnId" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="TaxTp" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Authstn" type="TaxAuthorisation1"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="TaxPeriod1">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="Yr" type="ISODate"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Tp" type="TaxRecordPeriod1Code"/>
            <xs:element maxOccurs="1" minOccurs="0" name="FrToDt" type="DatePeriodDetails"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="TaxRecord1">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="Tp" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Ctgy" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="CtgyDtls" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="DbtrSts" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="CertId" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="FrmsCd" type="Max35Text"/>
            <xs:element maxOccurs="1" minOccurs="0" name="Prd" type="TaxPeriod1"/>
            <xs:element maxOccurs="1" minOccurs="0" name="TaxAmt" type="TaxAmount1"/>
            <xs:element maxOccurs="1" minOccurs="0" name="AddtlInf" type="Max140Text"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="TaxRecordDetails1">
        <xs:sequence>
            <xs:element maxOccurs="1" minOccurs="0" name="Prd" type="TaxPeriod1"/>
            <xs:element name="Amt" type="ActiveOrHistoricCurrencyAndAmount"/>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="TaxRecordPeriod1Code">
        <xs:restriction base="xs:string">
            <xs:enumeration value="MM01"/>
            <xs:enumeration value="MM02"/>
            <xs:enumeration value="MM03"/>
            <xs:enumeration value="MM04"/>
            <xs:enumeration value="MM05"/>
            <xs:enumeration value="MM06"/>
            <xs:enumeration value="MM07"/>
            <xs:enumeration value="MM08"/>
            <xs:enumeration value="MM09"/>
            <xs:enumeration value="MM10"/>
            <xs:enumeration value="MM11"/>
            <xs:enumeration value="MM12"/>
            <xs:enumeration value="QTR1"/>
            <xs:enumeration value="QTR2"/>
            <xs:enumeration value="QTR3"/>
            <xs:enumeration value="QTR4"/>
            <xs:enumeration value="HLF1"/>
            <xs:enumeration value="HLF2"/>
        </xs:restriction>
    </xs:simpleType>
</xs:schema>
'''
