using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace PetProject2.Models
{
    public class FakePetRepository : IPetsRepository
    {
        public IQueryable<Pet> Pets => new List<Pet> {
        new Pet { pet_name = "Football", pet_photo = "link" },
        new Pet {pet_name = "Football", pet_photo = "link" },
        new Pet {pet_name = "Football", pet_photo = "link" }
        }.AsQueryable<Pet>();
            }
}
