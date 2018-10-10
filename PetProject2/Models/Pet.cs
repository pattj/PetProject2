using CsvHelper.Configuration;
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace PetProject2.Models
{
    public class Pet
    {
        [Key]
        public string pet_name { set; get; }
        public string pet_photo { set; get; }
        public char pet_gender { set; get; }
        public string pet_description { set; get; }
        public string pet_lastupdated { set; get; }
        public string pet_type { set; get; }
        public int AnimalID { get; set; }
        public string shelter_id { set; get; }
        public string pet_breed1 { set; get; }
        public string pet_breed2 { set; get; }
        public string pet_detail { set; get; }

    }

    public sealed class PetMap : ClassMap<Pet>
    {
        public PetMap()
        {
             
            Map(m => m.pet_name);
            Map(m => m.pet_photo);
            Map(m => m.pet_gender);
            Map(m => m.pet_description);
            Map(m => m.pet_type);
            Map(m => m.AnimalID);
            Map(m => m.shelter_id);
            Map(m => m.pet_breed1);
            Map(m => m.pet_breed2);
            Map(m => m.pet_detail);
        }
         
    }
}
