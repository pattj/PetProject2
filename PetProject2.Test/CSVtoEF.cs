using System;
using Xunit;
using PetProject2.Models;
using System.IO;
using Xunit.Abstractions;

namespace PetProject2.Test
{
    public class CSVtoEF
    {

        private readonly ITestOutputHelper output;

        public  CSVtoEF(ITestOutputHelper output)
        {
            this.output = output;
        }

        [Fact]
        public void Test1()
        {
            //var textReader = new StringReader(Properties.Resources.Pets);
             
            var test = SeedData.testSeed();
            int count = test.Count;
 
            Assert.Equal( "Anibelle", test[0].pet_name);
            Assert.Equal("Tabby", test[0].pet_breed1);
            Assert.Equal(string.Empty, test[0].pet_breed2);
            Assert.Equal("housetrained", test[0].pet_detail);
            Assert.Equal('F', test[0].pet_gender);
            Assert.Equal("2017-07-24T10:24:20+00:00", test[0].pet_lastupdated);
            Assert.Equal("{'photo': [{'@size': 'pnt', '$t': 'http://photos.petfinder.com/photos/pets/38856095/1/?bust=1516454067&width=60&-pnt.jpg', '@id': '1'}, {'@size': 'fpm', '$t': 'http://photos.petfinder.com/photos/pets/38856095/1/?bust=1516454067&width=95&-fpm.jpg', '@id': '1'}, {'@size': 'x', '$t': 'http://photos.petfinder.com/photos/pets/38856095/1/?bust=1516454067&width=500&-x.jpg', '@id': '1'}, {'@size': 'pn', '$t': 'http://photos.petfinder.com/photos/pets/38856095/1/?bust=1516454067&width=300&-pn.jpg', '@id': '1'}, {'@size': 't', '$t': 'http://photos.petfinder.com/photos/pets/38856095/1/?bust=1516454067&width=50&-t.jpg', '@id': '1'}]}", test[0].pet_photo);
            Assert.Equal("NV48", test[0].shelter_id);
            Assert.Equal("Cat", test[0].pet_type);
            
        }
    }
}
