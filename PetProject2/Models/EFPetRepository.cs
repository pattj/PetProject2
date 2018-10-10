using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace PetProject2.Models
{
    public class EFPetRepository : IPetsRepository
    {
        private ApplicationDbContext context;

        public EFPetRepository(ApplicationDbContext ctx)
        {
            context = ctx;
        }

        public IQueryable<Pet> Pets => context.Pets;
    }
}
