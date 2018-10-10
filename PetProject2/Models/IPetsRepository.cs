using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace PetProject2.Models
{
    public interface IPetsRepository
    {
        IQueryable<Pet> Pets { get; }
    }
}
