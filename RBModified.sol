pragma solidity >=0.4.0 <0.7.0;

contract RBX {
    uint256 public transactionCount = 0;
    uint256 public newcount = 0;
    mapping (uint => RiceInfo) AllRice;
    mapping (uint => RiceInfo) RiceAll;
    mapping (string => AccountInfo) AllAccount;

    // data handling
    struct RiceInfo {
        uint _StoreId;
        string _User;
        string _Manufacturer;
        string _Brand;
        string _Area;
        string _Status;
        string _StatusRecieved;
        uint _StatusWeight;
        uint _Date;
        uint _Year;
        uint _Month;
        uint _Day;
        uint _Weight; // weight per kilo
        uint _Price;  // srp price per kg
    }

    // account handling
    struct AccountInfo {
        string Password;
    }

    //function to increase the transaction count by 1 per added transaction
    function incrementCount() internal{
        transactionCount += 1;
        newcount += 1;
    }

    // function to get latest transactionCount
    function getTransID() public view returns (uint){
        return newcount;
    }

    //function to accept input from user
    function enterRiceInfo(string memory _User, string memory _Manufacturer, string memory _Brand, string memory _Area,
    string memory _Status, string memory _StatusRecieved, uint _StatusWeight,
    uint _Date, uint _Year, uint _Month, uint _Day, uint _Weight, uint _Price) public {
        incrementCount();
		AllRice[transactionCount] = RiceInfo(transactionCount, _User, _Manufacturer, _Brand, _Area, _Status, _StatusRecieved, _StatusWeight,
        _Date, _Year, _Month, _Day, _Weight, _Price );
		RiceAll[_Date] = RiceInfo(transactionCount, _User, _Manufacturer, _Brand, _Area, _Status, _StatusRecieved, _StatusWeight,
        _Date, _Year, _Month, _Day, _Weight, _Price);
    }

    //function to get the manufacturer
    function getManu(uint _StoreId) public view returns (string memory){
        return (AllRice[_StoreId]._Manufacturer);
    }

    //function to get the Brand
    function getBrand(uint _StoreId) public view returns (string memory){
        return (AllRice[_StoreId]._Brand);
    }

    //function to get the area of every transaction
    function getArea(uint _StoreId) public view returns (string memory){
        return (AllRice[_StoreId]._Area);
    }

    //function to get the status of every transaction
    function getStatus(uint _StoreId) public view returns (string memory){
        return (AllRice[_StoreId]._Status);
    }

    //function to get the status recieved of every transaction
    function getStatusRecieved(uint _StoreId) public view returns (string memory){
        return (AllRice[_StoreId]._StatusRecieved);
    }

    //function to get the status recieved of every transaction
    function getStatusWeight(uint _StoreId) public view returns (uint){
        return (AllRice[_StoreId]._StatusWeight);
    }

    //since this is used in a function to get the date for looping, this can only output dates in YYYYMMDD format
    function getDate(uint _StoreId) public view returns (uint){
        return (AllRice[_StoreId]._Date);
    }

    //This is the function to get the Year
    function getYear(uint _StoreId) public view returns (uint){
        return (AllRice[_StoreId]._Year);
    }

    //This is the function to get the Month
    function getMonth(uint _StoreId) public view returns (uint){
        return (AllRice[_StoreId]._Month);
    }

    //This is the function to get the Day
    function getDay(uint _StoreId) public view returns (uint){
        return (AllRice[_StoreId]._Day);
    }

    //function to get the weight
    function getWeight(uint _StoreId) public view returns (uint){
        return (AllRice[_StoreId]._Weight);
    }

    //function to get the price
    function getPrice(uint _StoreId) public view returns (uint){
        return (AllRice[_StoreId]._Price);
    }

    //function to get the user who entered the transaction
    function getUser(uint _StoreId) public view returns (string memory){
        return (AllRice[_StoreId]._User);
    }


    // function to register
    function Register(string memory _UserName, string memory _Password) public {
        AllAccount[_UserName].Password = _Password;
    }

    // function to login
    function Login(string memory _UserName) public view returns (string memory) {
        return(AllAccount[_UserName].Password);
    }

}